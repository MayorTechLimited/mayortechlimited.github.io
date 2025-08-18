import puppeteer from "puppeteer";

async function run() {
    const browser = await puppeteer.launch({
        executablePath: "/usr/bin/chromium",
        args: [
            "--no-sandbox",
            "--headless",
            "--disable-gpu",
            "--font-render-hinting=none",
        ],
    });
    const page = await browser.newPage();

    await page.setRequestInterception(true);
    page.on("request", (request) => {
        const headers = {
            ...request.headers(),
            Origin: "https://www.mayortech.co.uk",
        };
        request.continue({
            headers: headers,
        });
    });
    await page.goto("file:///app/dist/cv/index.html", {
        waitUntil: "networkidle0",
    });
    await page.pdf({
        path: "/app/dist/William Mayor's CV.pdf",
        format: "A4",
        margin: {
            top: "0px",
            left: "0px",
            right: "0px",
            bottom: "0px",
        },
        printBackground: true,
    });
    await browser.close();
}

run();
