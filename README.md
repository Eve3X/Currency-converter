## Currency Converter App
This is a simple currency converter application with the ability to plot historical currency values against time.

## Prerequisites
Make sure you have the following installed:

Python (version 3.x)
Required Python packages: tkinter, pandas, matplotlib
Install the required packages using the following command:

```bash

pip install pandas matplotlib
```
## Northern Trust Project
 
Firstly we import all the important libraries needed for showing graphs and file handling,
we have used popular libraries like pandas and matplotlib.
In our csv there was some inconsistent data and to make it uniform and we have split the columns to only print the ISO format of currencies.
Following the above step, we have downloaded the updated csv after the heading and read it again for future uses.
Below we have combined the csv files of all 10 years to form a single csv file with the help of the os.path library that provides a platform-independent way of working with file paths. Then we have created a new empty dataframe and in a loop we have started concatenated all the datasets of previous years.
After we have combined the files we have downladed the combined file.
After the above step, we read the combined file and sort the file according to dates, making it easier to track weekly, monthly and years changes.
Then Tested out the first graph on the combined dataframe of all currencies.
Plotting graph for overall change for a currency.We have also shown the min and max value of the respective currency.
We also made a default calculator on a the colab file just for rerfernce.
test.py defines a simple currency converter application using Tkinter for the GUI, allowing users to convert USD to a specified currency, select a currency for historical data, choose a duration (weekly, monthly, etc.), and plot a historical currency value graph against time. The application retrieves currency data from a CSV file, and users can visualize historical trends, identify peak and low values, and perform quick USD conversions. The code utilizes pandas for data manipulation and matplotlib for plotting.
![1](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/4ddf6e7e-87d7-468d-8a80-9a4f5c47c738)

![2](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/a775b0fe-04aa-40e7-b33a-a04fa52c9b9d)
![7](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/a9fa802f-9423-497e-9d3a-ed3f1683a3dc)

![6](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/90693a02-0d9b-4edb-99d1-84e7425a2244)
![5](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/83888bc5-1738-4ba3-8792-abfcbfc48e5d)
![4](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/1899afc5-9162-4e1c-ae6b-a35427dc14a8)
![3](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/d70c2e35-a084-45e1-8c26-563b27a19f27)

## Getting Started
Clone or download the repository.
```bash

git clone https://github.com/your-username/currency-converter-app.git
```
## Navigate to the project directory.
```bash

cd currency-converter-app

```
## Run the application.
```bash

python currency_converter.py
```
## Usage
The application window will appear with options to convert USD, select a currency, choose a duration, and plot a graph.

Convert USD:

Input the currency you want to convert USD to in the provided entry field.
Click the "Convert" button to see the conversion result.
Select Currency:

Input the currency you want to plot historical data for in the provided entry field.
Select Duration:

Choose the desired duration for the historical data (Weekly, Monthly, Quarterly, Yearly, Decade) using the dropdown.
Plot Graph:

Click the "Plot Graph" button to generate and display a historical plot for the selected currency and duration.

## Alternate approach (couldn't complete)
We also tried a different UI using React but were unable to link it to our backend, because of lack of experience in flask we were unable to move ahead with it, but below are the screenshots for our React UI-


![react2](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/b342ae31-b80b-4c1f-8f8a-e01e8a492bec)
![react3](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/647eb260-209e-457c-951a-b8016a518a42)
![react1](https://github.com/AjinkyaD-21/MITWPU-TEAM19-PROJECT/assets/91340947/eb07e737-f4de-4989-bcad-720cc6afabc9)

