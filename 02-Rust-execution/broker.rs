use reqwest::{blocking::Client, header::{HeaderMap, HeaderValue, USER_AGENT}};
use hmac::{Hmac, Mac};
use sha2::Sha256;
use base64::encode;
use serde_json::json;
use std::time::{SystemTime, UNIX_EPOCH};
use std::error::Error;
use serde_urlencoded;

type HmacSha256 = Hmac<Sha256>;

pub struct KucoinApi {
    key: String,
    secret: String,
    passphrase: String,
    base_url: String,
}

impl KucoinApi {
    pub fn new(key: String, secret: String, passphrase: String) -> Self {
        KucoinApi {
            key,
            secret,
            passphrase,
            base_url: "https://api-futures.kucoin.com".to_string(),
        }
    }

    fn generate_signature(&self, method: &str, uri: &str, params: Option<String>, timestamp: u64) -> String {
        let mut str_to_sign = timestamp.to_string() + method + uri;
        if let Some(p) = params {
            str_to_sign.push_str(&p);
        }

        let mut mac = HmacSha256::new_from_slice(self.secret.as_bytes())
            .expect("HMAC creation failed");
        mac.update(str_to_sign.as_bytes());
        let result = mac.finalize().into_bytes();
        encode(&result)
    }

    pub fn request(
        &self,
        method: &str,
        uri: &str,
        params: Option<serde_json::Value>,
    ) -> Result<serde_json::Value, Box<dyn Error>> {
        let client = Client::new();
        let timestamp = SystemTime::now().duration_since(UNIX_EPOCH)?.as_millis() as u64;
        let uri_path = if let Some(p) = &params {
            format!("{}?{}", uri, serde_urlencoded::to_string(p)?)
        } else {
            uri.to_string()
        };

        let signature = self.generate_signature(method, &uri_path, params.as_ref().map(|p| p.to_string()), timestamp);

        let mut headers = HeaderMap::new();
        headers.insert("KC-API-SIGN", HeaderValue::from_str(&signature)?);
        headers.insert("KC-API-TIMESTAMP", HeaderValue::from_str(&timestamp.to_string())?);
        headers.insert("KC-API-KEY", HeaderValue::from_str(&self.key)?);
        headers.insert("KC-API-PASSPHRASE", HeaderValue::from_str(&self.passphrase)?);
        headers.insert(USER_AGENT, HeaderValue::from_static("kucoin-rust-sdk/v1.0.0"));

        let request = client
            .request(method.parse()?, &format!("{}{}", self.base_url, uri_path))
            .headers(headers);

        let response = if let Some(p) = &params {
            request.json(p).send()?
        } else {
            request.send()?
        };

        let status = response.status();
        let response_body_text = response.text()?;
        let response_body: serde_json::Value = serde_json::from_str(&response_body_text)?;

        match status {
            reqwest::StatusCode::OK => Ok(response_body),
            _ => Err(format!("API request failed: {}", response_body).into()),
        }
    }

    pub fn get(&self, uri: &str) -> Result<serde_json::Value, Box<dyn Error>> {
        self.request("GET", uri, None)
    }

    pub fn post(&self, uri: &str, params: serde_json::Value) -> Result<serde_json::Value, Box<dyn Error>> {
        self.request("POST", uri, Some(params))
    }
}

