mod broker;
mod get_positions;


use broker::KucoinApi;
use std::error::Error;
use serde_json::Value; 


fn main() -> Result<(), Box<dyn Error>> {
    // Call the get_positions function and handle the result
    match get_positions::get_positions() {
        Ok(response) => {
            println!("{:?}", response);
        }
        Err(err) => {
            println!("Error: {}", err);
        }
    }

    Ok(())
}