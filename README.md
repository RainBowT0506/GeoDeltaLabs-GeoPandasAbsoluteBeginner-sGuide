實作影片 [GeoDelta Labs - Introduction to GIS Analysis with GeoPandas using Python](https://www.youtube.com/watch?v=t7lliJXFt8w)

Github：[GeoDeltaLabs-GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide)

## Districts Plot
![Districts Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/1482d362-7c08-4997-b6c7-8e418ace75be)

## Area of Interest Plot
![Area of Interest Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/6fe1cfca-03f6-4b95-8b1c-51b53f0e6f21)

## Districts and Area of Interest Plot
![Districts and Area of Interest Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/e23b0140-6720-415f-9a47-065387ccb570)

## Multiple Layers Plot
![Multiple Layers Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/e7ad7a7a-0cd1-41b7-98b4-7a07d124c276)

## Reprojected GeoDataFrames Plot
![Reprojected GeoDataFrames Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/97a2df75-1008-4bdd-808d-10b826fd2ee3)

## Intersected Layers Plot
![Intersected Layers Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/96f9d246-8041-48f6-a830-99e3aebaeb90)


## Introduction 
使用 GeoPandas Python 庫開始處理地理空間數據所需的基本但非常重要的事項。我們將涵蓋各種主題，從教你如何安裝或配置 GeoPandas 库，到執行地理空間操作並在 Python 中使用 GeoPandas 库創建引人注目的地理空間數據圖。

1. 安裝和配置 GeoPandas 库
1. 地理空間操作的基本知識
1. 在 Python 中使用 GeoPandas 库進行地理空間操作
1. 創建吸引人的地理空間數據圖
## Installing Geopandas Library 
使用 Anaconda Prompt 安裝 GeoPandas
1. 確保你已經安裝了 Anaconda 發行版。
2. 開啟 Anaconda Prompt（以管理員身分運行）。
3. GeoPandas 需要一些依賴庫，使用 conda 可以方便安裝這些依賴庫，無需手動處理。在 Anaconda Prompt 中執行以下指令：
    ```bash
    conda install geopandas
    ```
4. 此過程可能需要一些時間，取決於你的網速和系統性能。
5. 一旦出現提示是否繼續，輸入 `y` 表示確認安裝。
6. 安裝完成後，需要額外安裝一個用於繪圖的庫 descartes。在 Anaconda Prompt 中執行以下指令：
    ```bash
    pip install descartes
    ```
7. 現在，GeoPandas 和 descartes 都已成功安裝，你可以開始使用 GeoPandas 開展地理空間數據的處理和繪圖操作。

## Introducing Spyder IDE
### 驗證 GeoPandas 是否正確安裝
1. 打開 Spyder IDE。
2. 在 Spyder 的編輯器中輸入以下代碼，確認是否成功安裝 GeoPandas：
3. 沒有出現錯誤的情況下，代表 GeoPandas 已經成功安裝。
4. 若要查看 GeoPandas 庫的內容，可以使用 `help` 函數：

### Spyder IDE 介紹
1. Code Editor: 這是你的代碼編輯器，用於編寫和運行 Python 代碼。
2. IPython Console: 這是一個互動式的 Python 控制台，你可以在這裡進行快速操作，並查看運行結果。
3. Variable Explorer: 這個選項卡會顯示你的變量，讓你可以方便地查看和管理它們。
4. History, Help, Plots, Files: 這些選項卡提供了對文件、歷史記錄、幫助和繪圖的訪問。

### 開始使用 Spyder IDE
1. 導航到你存放教程文件的文件夾。
2. 在 "Files" 選項卡中，使用文件夾圖標選擇文件夾。
3. 創建一個新的 Python 腳本：右鍵單擊空白處 -> New -> Python Script。
4. 將腳本保存在指定文件夾中，例如 "intro_to_geopandas.py"。
5. 在腳本中導入 GeoPandas：
6. 你現在可以在 Spyder IDE 中使用 GeoPandas 進行地理空間數據的處理和分析。
## Creating a new Python Script 
1. 在 Spyder 中，找到 "Files" 選項卡。
2. 在空白處右鍵單擊，然後選擇 "New"。
3. 在彈出的菜單中選擇 "Python Script"。
4. 現在，為腳本命名。例如，我們可以將其命名為 `intro_to_geo_pandas.py`。
5. 點擊 "Save" 保存腳本，確保它保存在 "Introduction to GeoPandas" 文件夾中。

## Import ESRI Shapefiles into Python using Geopandas
1. 打開 Spyder IDE，確保已經成功安裝 GeoPandas。
2. 找到你存放 ESRI Shapefiles 的文件夾。
3. 在文件夾中選擇你想要導入的 Shapefile，例如 `districts.shp`。
4. 在 Spyder 的編輯器中，創建一個新的 Python 腳本，並使用以下代碼導入 GeoPandas：
5. 創建一個變量來存儲 Shapefile 中的數據，例如：
   記得替換 `path/to/your/shapefile` 為你的實際文件夾路徑。
6. 保存腳本，運行文件。你可以點擊 "Run File" 按鈕或按下 `F5`。
7. 在 IPython Console 中，輸入 `districts` 查看讀取的數據。
8. 如果想查看變量的類型，可以輸入 `type(districts)`。
9. 若要在 Variable Explorer 中查看變量，可以點擊左邊的 "Variable Explorer" 選項卡。
10. 這樣你就成功導入 Shapefile 數據並創建了 GeoPandas GeoDataFrame。
11. 注意，GeoDataFrame 中的 `geometry` 列包含了地理空間信息，請不要刪除它，以免丟失空間數據的屬性。
## Basic plotting using Geopandas
使用 GeoPandas 進行基本的繪圖。首先，我們將繪製來自兩個 ESRI Shapefiles 的地理空間數據。
1. 打開新的 Python 腳本，將其保存為 `plotting_example.py`。
2. 導入 GeoPandas 庫：
3. 導入 ESRI Shapefiles 並創建 GeoDataFrames：
4. 使用 `plot` 函數繪製地理空間數據：
5. 執行腳本並查看生成的圖形。

![Districts Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/1482d362-7c08-4997-b6c7-8e418ace75be)

![Area of Interest Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/6fe1cfca-03f6-4b95-8b1c-51b53f0e6f21)

## Multiple Plots (Side-by-side)
使用 GeoPandas 和 Matplotlib 在同一圖中繪製多個圖層。
1. 打開新的 Python 腳本，將其保存為 `multiple_layers_plot.py`。
2. 導入 GeoPandas 和 Matplotlib：
3. 導入 ESRI Shapefiles 並創建 GeoDataFrames：
    記得替換 `path/to/your/shapefile` 為實際文件夾路徑。
4. 使用 Matplotlib 在同一圖中繪製多個圖層：
5. 執行腳本並查看生成的圖形。

![Districts and Area of Interest Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/635fd3be-3c8d-4238-bb2b-0593f2a277bd)

## Multiple layers on the same figure 
使用 GeoPandas 在同一圖中繪製多個圖層。我們將繼續使用 Matplotlib 來進行進階的繪圖操作。

1. 打開新的 Python 腳本，將其保存為 `multiple_layers_plot.py`。
2. 導入 GeoPandas 和 Matplotlib：
3. 導入 ESRI Shapefiles 並創建 GeoDataFrames：
4. 使用 Matplotlib 在同一圖中繪製多個圖層：

![Multiple Layers Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/e7ad7a7a-0cd1-41b7-98b4-7a07d124c276)

## Working with projections in Geopandas
更改 GeoPandas 中圖層的坐標參考系統（投影）。我們將將區域（districts）圖層轉換為英國常用的投影坐標參考系統 UTM Zone 29。

1. 打開新的 Python 腳本，將其保存為 `multiple_layers_projection.py`。
2. 導入 GeoPandas 和 Matplotlib：
3. 導入 ESRI Shapefiles 並創建 GeoDataFrames：
4. 轉換坐標參考系統（Projection）：
    在這裡，我們使用 `to_crs` 方法來將 GeoPandas 圖層轉換為指定的坐標參考系統（EPSG 32629）。
5. 使用 Matplotlib 在同一圖中繪製多個圖層：

![Reprojected GeoDataFrames Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/97a2df75-1008-4bdd-808d-10b826fd2ee3)

## Intersecting layers using Geopandas 
使用 GeoPandas 進行兩個圖層的交叉分析。具體來說，我們將交叉分析 "districts" 圖層和 "area_of_interest" 圖層，以了解哪些區域落在我們感興趣的區域內。

1. 打開新的 Python 腳本，保存為 `intersect_layers.py`。
2. 導入 GeoPandas 和 Matplotlib：
3. 導入 ESRI Shapefiles 並創建 GeoDataFrames：
4. 進行圖層交叉分析：
    在這裡，我們使用 `gpd.overlay` 函數進行圖層的交叉分析。`how='intersection'` 表示我們要進行交集操作。
5. 繪製交叉分析結果：
    使用 `gpd.overlay` 的結果 `districts_in_aoi` 來繪製交叉分析的結果。我們使用紅色的邊線顯示位於區域內的各個區域。

![Intersected Layers Plot](https://github.com/RainBowT0506/GeoDeltaLabs-GeoPandasAbsoluteBeginnersGuide/assets/109667537/96f9d246-8041-48f6-a830-99e3aebaeb90)

## Geometrical computations (calculating areas of polygons)
使用 GeoPandas 計算多邊形的面積。我們將在 `districts_in_aoi` 圖層上執行這個任務，該圖層代表了區域內的各個行政區。

1. 打開之前的 Python 腳本（`intersect_layers.py`）。
2. 在腳本頂部，導入必要的庫：
3. 現在，在計算面積之前，我們需要為 `districts_in_aoi` 圖層添加一個新的列，用於存儲面積：
    在這裡，我們使用 `districts_in_aoi.area` 來計算多邊形的面積，然後將其除以 1e6 以將平方米轉換為平方公里。
4. 現在，我們可以重新運行繪圖的代碼，以查看更新的面積信息：
    在這裡，我們將 `districts_in_aoi` 圖層的 `area` 列指定為 `column='area'`，以在繪圖時使用這些面積信息。

## Exporting Geopandas GeoDataFrames into ESRI Shapefiles 
使用 GeoPandas 將 GeoDataFrames 匯出為 ESRI Shapefiles。我們將使用 `districts_in_aoi` GeoDataFrame 作為範例。
1. 打開之前的 Python 腳本。
2. 在腳本頂部，導入必要的庫：
3. 在腳本的最後部分，添加一個新的標題，稱為 "Exporting to ESRI Shapefiles"。
4. 現在，我們將 `districts_in_aoi` GeoDataFrame 匯出為 ESRI Shapefile：
    在這裡，我們使用 `to_file` 方法，將 GeoDataFrame 匯出為 ESRI Shapefile。輸入的參數是 ESRI Shapefile 的檔案路徑，這裡我們指定為 `districts_within_aoi.shp`。
5. 現在你可以運行整個腳本。
6. 如果成功運行，你應該能夠在腳本的工作目錄中找到一個名為 `districts_within_aoi.shp` 的 ESRI Shapefile。
    完成了 GeoDataFrame 的匯出。你可以使用這個 Shapefile 進行其他 GIS 工具中的分析或與他人分享。確保在運行腳本之前保存它。
    
## 關鍵字
1. GeoPandas（地理資料框）： 一個建立在NumPy、Pandas、Shapely、Fiona和Matplotlib等庫之上的Python庫，用於處理地理空間數據。
2. Anaconda（安納科達）： 一個開源的Python發行版和管理器，包含許多用於科學計算的庫和工具，被用來安裝GeoPandas。
3. Shapefile（SHP檔案）： 一種空間數據文件格式，通常用於存儲地理信息，包括點、線和多邊形等地理實體。
4. Conda（康達）： Anaconda的包管理器，用於安裝和管理Python庫及其依賴項。
5. GeoDataFrame（地理資料框）： GeoPandas中的一個特殊數據結構，類似於Pandas的DataFrame，但包含地理空間信息。
6. Cmap（Color Map）： Color Map的縮寫，指定地理實體根據某一列的值使用不同的顏色。
7. Matplotlib（馬特布利布）： 一個Python數據可視化庫，GeoPandas利用其繪圖功能實現地理空間數據的視覺化。
8. Latitude（緯度）和Longitude（經度）： 表示地理坐標的橫線和縱線，用來定位地球表面的點。
9. Spatial Data（空間數據）： 具有地理信息的數據，通常包括地理實體的位置和形狀。
10. Shapefile Folder（SHP檔案文件夾）： 包含一個或多個Shapefile文件的文件夾，用於存儲地理空間數據。
11. IPython Console（互動式Python控制台）： Spyder集成開發環境中的互動式Python控制台，用於執行快速操作和檢查變量。
12. Color Scheme或Color Map（顏色方案或顏色映射）： 一組用於指定數據值與顏色之間映射的規則。
13. Edge Color（邊界顏色）： 地理實體之間邊界的顏色，用於區分不同的地理實體。
14. Coordinate Reference System（CRS，座標參考系統）： 一種數學模型，用來表示地理位置的坐標系統，確保地理資料在地球上的正確位置。
15. EPSG Code（EPSG代碼）： 國際石油勘探協會（International Petroleum Exploration and Production Association）制定的一套地理資訊相關的標準代碼，用來標識不同的座標參考系統。
16. Reprojection（重投影）： 將地理資料從一個座標參考系統轉換為另一個座標參考系統的過程。
17. Overlay（重疊）： 將兩個地理資料圖層合併在一起，通常用於計算它們的交集、聯集等操作。
18. Intersect（相交）： 兩個地理圖層之間的幾何相交操作，用於確定兩者之間的重疊部分。
19. Geoprocessing（地理處理）： 在地理資訊科學中，對地理資料進行分析、操作和轉換的過程，通常包括空間查詢、地理統計等操作。
20. Buffer（緩衝區）： 地理資料處理中的一種操作，用來在地理特徵周圍生成一個區域，通常用於分析某一區域的影響範圍。
21. Projection（投影）： 將三維地球表面的點映射到二維平面上的過程，有很多種不同的投影方法，每種方法都有其特定的用途和限制。
