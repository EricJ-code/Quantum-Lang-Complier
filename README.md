# Quantum-Lang-Complier
A language to learn quantum computing.

<br>
<p align="center">
  <a alt="Contributors"> <img src="https://img.shields.io/badge/Contributors-4-blue" /></a>
  <img src="https://img.shields.io/badge/Development_Stage-Beta-orange"
  <a href="https://github.com/BabyKangaroo117/Frugl-APP/graphs/contributors" alt="License">
        <img src="https://img.shields.io/badge/License-MIT-green" /></a>
</p>

## How it works
It creates Schrodinger's lanugage takes in a file, following the language specifications. From here, run the script and receive the necessary outputs. It is ran as a Powershell script. 

## Table of Contents

- [Screenshot](#screenshot)
- [Demo](#demo)
  - [How it Works](#how-it-works)
  - [Preview of Language File](#preview-of-language-file)
  - [Results](#results)
- [Install and Run](#install-and-run)
  - [Downloads](#downloads)
  - [Configure Venv](#configure-venv)
  - [Run Application](#run-application)
 
## Screenshot

## Demo

### How it Works
The language works by using a Powershell script. From here, a Racket script is called that converts our language into Python. The Python code is then excuted in the terminal, and displayed to the user.


### Preview of Data

### Results

## Install and Run
Download this folder which contains each of the necessary scripts to run our language.
You need to run the following commands in Windows Powershell. You need to locate the environment for Racket, the Powershell script, the Racket script, and the Python output file. Using all of these, input them into Powershell. <br> <br>
Here is an example input on how to run it in the script: <br>
.\SchrodingerScript.ps1 -RacketExecutablePath "C:\Program Files\Racket\Racket.exe" -RacketScriptPath "C:\Program Files\Coding Applications\Racket Scripts\SchrodingerLanguageMain.rkt" -InputFilePath "C:\Users\tyler\OneDrive\Documents\ExampleSchrodingerLanguage.txt" -OutputFilePath "C:\Users\tyler\OneDrive\Documents\output.py"
