const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
    content: ["./src/**/_*.html", "./src/**/*.html"],
    safelist: ["admonition"],
    theme: {
        extend: {
            colors: {
                "mt-blue": "#4B3DE3",
                "mt-yellow": "#F7D848",
                "mt-red": "#F75D48",
                "mt-darkest-blue": "#090535",
                "mt-dark-blue": "#221E49",
                "mt-gray": "#DDDED8",
            },
            fontFamily: {
                sans: ["SpaceGrotesk", ...defaultTheme.fontFamily.sans],
            },
            screens: {
                print: { raw: "print" },
                screen: { raw: "screen" },
            },
        },
    },
    plugins: [require("@tailwindcss/typography")],
};
