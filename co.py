# geospatial data analysis using geopandas and shapely 

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import shapely
from shapely.geometry import Point, Polygon
from shapely.ops import nearest_points
from shapely.geometry import LineString
from shapely.geometry import MultiLineString
from shapely.geometry import MultiPoint
from shapely.geometry import MultiPolygon
from shapely.geometry import GeometryCollection

# set working directory

os.chdir('D:/Dissertation/Land_cover2020/Land_cove

