# Sales Optimizer

## Descirption

The retail stores always face a problem of tension between demand and supply. Sometimes they stock more products than it has demand or sales and sometimes they stock less than demand, due to which they either suffer from loss or dissatisfied customers. This problem can be solved using this software. It uses various inventory data to predict the sales pattern of the retail store so that the retail store can stock their products accordingly.

### Parameters Used:

- Item weight
- Item fat content
- Item fat content
- Item visibility
- Item type
- Item MRP
- Outlet establistment year
- Outlet size
- Outlet location.

## Libraries Used:

- Numpy
- Pandas
- Seaborn
- Scikit-learn

## Example

1. Place `sales_data.csv` (containing columns such as `Item_Weight`, `Item_Fat_Content`, `Item_Visibility`, `Item_Type`, `Item_MRP`, `Outlet_Identifier`, `Outlet_Establishment_Year`, `Outlet_Size`, `Outlet_Location_Type`, `Outlet_Type`, and `Item_Outlet_Sales`) in the project directory.
2. Run `python main.py`. The script preprocesses the data (fills missing weights, encodes categorical columns), trains a `RandomForestRegressor`, and prints dataset info and evaluation metrics to the console.
3. Two matplotlib windows open: a seaborn pairplot of the features, and a scatter plot comparing actual vs predicted `Item_Outlet_Sales` values.

## How to run on localhost

```sh
pip install numpy pandas seaborn scikit-learn matplotlib
python main.py
```
