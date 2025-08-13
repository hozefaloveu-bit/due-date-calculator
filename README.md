# Due Date Calculator (KivyMD)

Android app to calculate invoice due dates using either calendar days or business days.

## Features
- Input invoice date in formats: YYYY-MM-DD, DD-MM-YYYY, DD/MM/YYYY
- Add calendar days or business days
- Material Design (KivyMD) interface

## Build APK locally
```bash
pip install buildozer
buildozer android debug
```
APK will be in `bin/`.

## Auto GitHub Release
This repo includes a GitHub Actions workflow that automatically:
- Builds the APK on push to `main`
- Publishes it to GitHub Releases
- Gives a public download link