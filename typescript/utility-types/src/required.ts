interface Config {
    host?: string;
    port?: number;
    secure?: boolean;
}

type StrictConfig = Required<Config>;

const config: StrictConfig = {
    host: "localhost",
    port: 3000,
    secure: true,
};

console.log(config);
