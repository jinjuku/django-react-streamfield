const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = (env, argv) => {
  const config = {
    entry: {
      "django-react-streamfield": [
        "./django_react_streamfield/static_src/js/entry.js",
        "./django_react_streamfield/static_src/scss/entry.scss"
      ]
    },
    output: {
      path: path.resolve("django_react_streamfield/static"),
      filename: "js/[name].js",
      publicPath: "/static/"
    },
    module: {
      rules: [
        {
          test: /\.jsx?$/,
          loader: "babel-loader",
          exclude: /node_modules/
        },
        {
          test: /\.scss$/,
          use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
        }
      ]
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: "css/[name].css",
        chunkFilename: "css/[id].css"
      })
    ]
  };
  return config;
};
