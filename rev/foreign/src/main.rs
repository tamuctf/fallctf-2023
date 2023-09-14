use hex_literal::hex;
use rand::{Rng, SeedableRng};
use tokio::io::{AsyncWriteExt, stdout};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let mut rng = rand_chacha::ChaChaRng::from_seed(hex!("00edcdb3f59cec20deb55ef7652c276904afe71554d11f18898ced1475fcb003"));
    const FLAG: [u8; 31] = hex!("de63b8f8e1ed00c808486ab643f5b00cf8e3a2098da5facbd2d2712f0d859e");

    let mut res = [0u8; FLAG.len()];
    rng.fill(&mut res);

    for (r, f) in res.iter_mut().zip(FLAG) {
        *r ^= f;
    }

    stdout().write_all(&res).await?;

    Ok(())
}
