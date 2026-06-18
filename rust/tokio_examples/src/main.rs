use tokio::io::{self, AsyncReadExt};
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;

    println!("running in 127.0.0.1:8080");

    loop {
        let (mut socket, _) = listener.accept().await?;

        println!("Client connect");

        tokio::spawn(async move {
            let mut buf = vec![0; 1024];

            loop {
                match socket.read(&mut buf).await {
                    Ok(0) => {
                        println!("Connection close");
                        return;
                    }
                    Ok(n) => {
                        let dados_recebidos = String::from_utf8_lossy(&buf[..n]);
                        println!("Received {} bytes: {}", n, dados_recebidos.trim());
                    }
                    Err(e) => {
                        println!("Error when try read socket: {:?}", e);
                        return;
                    }
                }
            }
        });
    }
}
