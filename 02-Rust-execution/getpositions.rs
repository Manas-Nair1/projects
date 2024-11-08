mod broker;

use broker::KucoinApi;
use std::error::Error;
use serde_json::Value; 

pub fn get_positions() -> Result<Value, Box<dyn Error>> {
    let api = KucoinApi::new(
        "".to_string(), //api key
        "".to_string(), //secret
        "".to_string(), //passphrase
    );

    // Perform the GET request for positions
    let response = api.get("/api/v1/positions")?;
    Ok(response)
}

