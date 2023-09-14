#![no_std]

use hex_literal::hex;
use rand::{Rng, SeedableRng};

fn main() -> anyhow::Result<()> {
    let mut rng = rand_chacha::ChaChaRng::from_seed(hex!("00edcdb3f59cec20deb55ef7652c276904afe71554d11f18898ced1475fcb003"));
    let mut key = [0u8; 64];
    rng.fill(&mut key);



    Ok(())
}
