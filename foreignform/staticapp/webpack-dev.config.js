const path = require('path');
const webpack = require('webpack');
const glob = require('glob');
const _ = require('lodash');

module.exports = port => ({
  resolve: {
    extensions: ['*', '.js', '.jsx', '.json'],
  },
  entry: _.zipObject(
    glob.sync('./src/js/main-*.js*').map(f => path.basename(f, path.extname(f))),
    glob.sync('./src/js/main-*.js*').map(f => [
      `webpack-hot-middleware/client?path=http://localhost:${port}/__webpack_hmr&reload=true`,
      f,
    ]),
  ),
  output: {
    path: '/',
    filename: 'js/[name].js',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: [
          {
          loader: 'babel-loader',
          options: {
            presets: [
              [
                '@babel/preset-env',
                {
                  targets: {
                    browsers: ['last 2 versions'],
                  },
                  debug: true,
                  modules: false,
                },
              ],
              '@babel/preset-react',
              'airbnb',
            ],
            plugins: [
              "@babel/plugin-proposal-function-bind",
            ],
          },
        },
        ],
      },
      {
        test: /\.(png|jpg|gif|ico)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
          use: {
            loader: 'file-loader',
          }
      },
      {
        test: /\.(ttf|eot|woff2|woff|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
          use: {
            loader: 'file-loader',
            options: {
              outputPath: 'fonts/bootstrap',
              name: '[name].[ext]'
            }
          }
      },
      {
        test: /\.scss$/,
        use: [
          'css-loader',
          'postcss-loader', 
          'resolve-url-loader',
          'sass-loader',
        ],
      },
    ],
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new webpack.ProvidePlugin({
      fetch: 'imports-loader?this=>global!exports-loader?global.fetch!whatwg-fetch',
    }),
  ],
  stats: 'minimal',
  devtool: 'cheap-module-eval-source-map',
  watch: true,
});
