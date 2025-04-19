name: Build Android APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v3

    - name: Instalar dependências
      run: |
        sudo apt update
        sudo apt install -y zip unzip openjdk-17-jdk python3-pip python3-setuptools git
        python3 -m pip install --upgrade pip
        pip install buildozer cython

    - name: Build APK
      run: |
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk-pix-veias
        path: bin/*.apk
