fn main() -> Result<(), Box<dyn Error>> {
    // Initialize Kucoin API credentials
    let kucoin_api = KucoinApi::new(
        "your_api_key".to_string(),
        "your_api_secret".to_string(),
        "your_api_passphrase".to_string(),
    );

    // Define order parameters
    let symbol = "XBTUSDTM";
    let side = "buy"; // "buy" or "sell"
    let price = 50000.0; // The price at which to buy
    let size = 1; // in lots

    // Create order request parameters
    let order_params = json!({
        "symbol": symbol,
        "side": side,
        "price": price,
        "size": size,
        "type": "limit",  // You can also use "market" for market orders
    });

    // Send the order request
    let response = kucoin_api.post("/api/v1/orders", order_params)?;

    // Print the response from Kucoin
    println!("Response: {}", response);

    Ok(())
}