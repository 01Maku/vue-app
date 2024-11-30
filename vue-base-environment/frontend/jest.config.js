module.exports = {
  preset: "@vue/cli-plugin-unit-jest",
  transform: {
    "^.+\\.vue$": "@vue/vue3-jest",
    "^.+\\.js$": "babel-jest",
  },
  moduleFileExtensions: ["js", "vue", "json"],
  testMatch: ["<rootDir>/tests/**/*.spec.js"],
  collectCoverage: true,
  collectCoverageFrom: ["src/**/*.{js,vue}", "src/App.vue", "!src/main.js"],
  coverageReporters: ["html", "text", "lcov"],
  coverageDirectory: "./coverage",
};
