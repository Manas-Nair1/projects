import os
import requests
import re
import argparse
import sys

class InsiderTradingAnalyzer:
    def __init__(self, index_file_path, form4s_path):
        self.index_file_path = index_file_path
        self.form4s_path = form4s_path

    def find_occurrences(self, name):
        index_file = open(self.index_file_path).readlines()
        find_list = []
        item = 0
        line = 0

        while line < len(index_file):
            i = index_file[line]
            if i.find(name) != -1:
                loc1 = i.find('13D')
                loc2 = i.find("13G") 
                loc3 = i.find("13E3")
                loc4 = i.find("13H")

                if (loc2 != -1) or (loc1 != -1) or (loc3 != -1) or (loc4 != -1):
                    find_list.append(i)
                    item += 1
                line += 1
            else:
                line += 1
        return item

    def find_form4(self, name):
        index_file = open(self.index_file_path).readlines()
        form4_list = []
        for line in index_file:
            loc = line.find(name)
            if loc != -1:
                try:
                    if '4' in line.split():
                        form4_list.append(line)
                except:
                    pass
        return form4_list

    def get_form4s(self, list_of_4s):
        links = ["https://www.sec.gov/Archives/" + item.split()[-1] for item in list_of_4s]
        os.chdir(self.form4s_path)

        def create_file(filename, content):
            name = str(filename) + ".txt"
            with open(name, "w") as file:
                file.write(str(content))
                file.close()
                print("Succeed!")

        unable_request = 0

        for a_index in range(len(links)):
            web_add = links[a_index]
            filename = a_index
            webpage_response = requests.get(web_add, headers={'User-Agent': 'Mozilla/5.0'})

            if webpage_response.status_code == 200:
                body = webpage_response.content
                create_file(filename, body)
            else:
                print("Unable to get response with Code : %d " % (webpage_response.status_code))
                unable_request += 1

            a_index += 1

        print(unable_request)

    def read_txt(self, file_name):
        txt_file = open(file_name, "r", encoding='UTF8')
        str_txt = txt_file.read()
        return str_txt

    def on_4(self, path, ticker):
        try:
            text = self.read_txt(path)
            pattern = r'<issuerTradingSymbol>(.*?)</issuerTradingSymbol>'
            issuer = re.findall(pattern, text, re.DOTALL)
            if issuer[0] == ticker:
                transaction_pattern = r'<transactionAcquiredDisposedCode>(.*?)</transactionAcquiredDisposedCode>'
                transaction = re.findall(transaction_pattern, text, re.DOTALL)
                value_pattern = r"<value>(.*?)</value>"
                code = re.findall(value_pattern, transaction[0], re.DOTALL)
            if issuer != ticker:
                print(issuer, path)
            return code[0]
        except:
            return None

    def on_all_4s(self, folderpath, ticker):
        codes = []
        for filename in os.listdir(folderpath):
            file_path = os.path.join(folderpath, filename)
            code = self.on_4(file_path, ticker)
            if code is not None:
                codes.append(code)
        return codes


def main():
    parser = argparse.ArgumentParser(description="Insider Trading Analyzer")
    parser.add_argument("company_name", help="Company name for analysis")
    parser.add_argument("ticker", help="Ticker symbol for analysis")
    parser.add_argument("--index_file_path", help="Path to the index file", default="/Users/manas/Documents/GitHub/trading/virtenv/Insider_buying/company.idx")
    parser.add_argument("--form4s_path", help="Path to the form4s directory", default="/Users/manas/Documents/GitHub/trading/virtenv/Insider_buying/form4s")

    args = parser.parse_args()

    # Create an instance of InsiderTradingAnalyzer
    insider_trading_analyzer = InsiderTradingAnalyzer(args.index_file_path, args.form4s_path)

    # Find occurrences
    occurrences = insider_trading_analyzer.find_occurrences(args.company_name)
    print(f"Occurrences for {args.company_name}: {occurrences}")

    # Find form4s
    form4s = insider_trading_analyzer.find_form4(args.company_name)
    print(f"Number of form4s for {args.company_name}: {len(form4s)}")

    # Get form4s
    insider_trading_analyzer.get_form4s(form4s)

    # Analyze all form4s
    all_codes = insider_trading_analyzer.on_all_4s(args.form4s_path, args.ticker)
    print(f"All codes for {args.ticker}: {all_codes}")

    # Delete all files in the form4s directory
    file_list = [f for f in os.listdir(args.form4s_path)]
    for file in file_list:
        file_path = os.path.join(args.form4s_path, file)
        os.remove(file_path)

if __name__ == "__main__":
    main()
# call as
# python3 /Users/manas/Documents/GitHub/trading/virtenv/Insider_buying/insider_buying_analysis.py "Pacira" "PCRX"