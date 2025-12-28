use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello {name}!"));
}

#[wasm_bindgen]
pub fn add(number1: i32, number2: i32) -> i32 {
    return number1 + number2;
}
