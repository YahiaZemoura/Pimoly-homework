{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as py\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase ID</th>\n",
       "      <th>SN</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Item ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Lisim78</td>\n",
       "      <td>20</td>\n",
       "      <td>Male</td>\n",
       "      <td>108</td>\n",
       "      <td>Extraction, Quickblade Of Trembling Hands</td>\n",
       "      <td>3.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Lisovynya38</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>143</td>\n",
       "      <td>Frenzied Scimitar</td>\n",
       "      <td>1.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Ithergue48</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>92</td>\n",
       "      <td>Final Critic</td>\n",
       "      <td>4.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Chamassasya86</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>100</td>\n",
       "      <td>Blindscythe</td>\n",
       "      <td>3.27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Iskosia90</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>131</td>\n",
       "      <td>Fury</td>\n",
       "      <td>1.44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Purchase ID             SN  Age Gender  Item ID  \\\n",
       "0            0        Lisim78   20   Male      108   \n",
       "1            1    Lisovynya38   40   Male      143   \n",
       "2            2     Ithergue48   24   Male       92   \n",
       "3            3  Chamassasya86   24   Male      100   \n",
       "4            4      Iskosia90   23   Male      131   \n",
       "\n",
       "                                   Item Name  Price  \n",
       "0  Extraction, Quickblade Of Trembling Hands   3.53  \n",
       "1                          Frenzied Scimitar   1.56  \n",
       "2                               Final Critic   4.88  \n",
       "3                                Blindscythe   3.27  \n",
       "4                                       Fury   1.44  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# Set path for file\n",
    "pymoli_csv = \"C:/Users/y-zem/Desktop/LearnPython/Pymoli/purchase_data.csv\"\n",
    "pymoli_df = pd.read_csv(pymoli_csv)\n",
    "pymoli_df.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Total Players'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Title = (\"Total Players\")\n",
    "Title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "780"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#\n",
    "Purchase_ID = pymoli_df.SN.count()\n",
    "Purchase_ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Purchase ID</th>\n",
       "      <th>SN</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Item_ID</th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Lisim78</td>\n",
       "      <td>20</td>\n",
       "      <td>Male</td>\n",
       "      <td>108</td>\n",
       "      <td>Extraction, Quickblade Of Trembling Hands</td>\n",
       "      <td>3.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Lisovynya38</td>\n",
       "      <td>40</td>\n",
       "      <td>Male</td>\n",
       "      <td>143</td>\n",
       "      <td>Frenzied Scimitar</td>\n",
       "      <td>1.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Ithergue48</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>92</td>\n",
       "      <td>Final Critic</td>\n",
       "      <td>4.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Chamassasya86</td>\n",
       "      <td>24</td>\n",
       "      <td>Male</td>\n",
       "      <td>100</td>\n",
       "      <td>Blindscythe</td>\n",
       "      <td>3.27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Iskosia90</td>\n",
       "      <td>23</td>\n",
       "      <td>Male</td>\n",
       "      <td>131</td>\n",
       "      <td>Fury</td>\n",
       "      <td>1.44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Purchase ID             SN  Age Gender  Item_ID  \\\n",
       "0            0        Lisim78   20   Male      108   \n",
       "1            1    Lisovynya38   40   Male      143   \n",
       "2            2     Ithergue48   24   Male       92   \n",
       "3            3  Chamassasya86   24   Male      100   \n",
       "4            4      Iskosia90   23   Male      131   \n",
       "\n",
       "                                   Item Name  Price  \n",
       "0  Extraction, Quickblade Of Trembling Hands   3.53  \n",
       "1                          Frenzied Scimitar   1.56  \n",
       "2                               Final Critic   4.88  \n",
       "3                                Blindscythe   3.27  \n",
       "4                                       Fury   1.44  "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pymoli_df = pymoli_df.rename(columns={\"Item ID\":\"Item_ID\", })\n",
    "\n",
    "pymoli_df.head()\n",
    "\n",
    "# Rename columns so that they are differentiated\n",
    "#crypto_df = crypto_df.rename(columns={\"Open_x\": \"Bitcoin Open\", \"High_x\": \"Bitcoin High\", \"Low_x\": \"Bitcoin Low\",\n",
    " #                                     \"Close_x\": \"Bitcoin Close\", \"Volume_x\": \"Bitcoin Volume\", \"Market Cap_x\": \"Bitcoin Market Cap\"})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "780"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count\n",
    "Item_ID = pymoli_df.Item_ID.count()\n",
    "Item_ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Players</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>576</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Total Players\n",
       "0            576"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player_count = len(pymoli_df[\"SN\"].value_counts())\n",
    "pd.DataFrame([player_count], columns = [\"Total Players\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Distinct Count\n",
    "Unique = pymoli_df.Item_ID.unique()\n",
    "Unique = pd.Series(Unique)\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "183"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Number_of_Unique_items = Unique.count()\n",
    "Number_of_Unique_items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.05"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Mean Revenue\n",
    "Mean_Revenue = pymoli_df[\"Price\"].mean()\n",
    "round(Mean_Revenue,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "780"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Number of Purchases\n",
    "Item_ID = pymoli_df.Item_ID.count()\n",
    "Item_ID"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2379.77"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Total Revenue\n",
    "Total_Revenue = pymoli_df[\"Price\"].sum()\n",
    "Total_Revenue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Number of Unique Items</th>\n",
       "      <th>Average Price</th>\n",
       "      <th>Number of Purchases</th>\n",
       "      <th>Total Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>183</td>\n",
       "      <td>3.050987</td>\n",
       "      <td>780</td>\n",
       "      <td>2379.77</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Number of Unique Items  Average Price   Number of Purchases  Total Revenue\n",
       "0                     183       3.050987                   780        2379.77"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create a summary data frame to hold the results\n",
    "\n",
    "\n",
    "# Creating a summary DataFrame using above values\n",
    "summary_df = pd.DataFrame({\"Number of Unique Items\":[Number_of_Unique_items],\n",
    "                            \"Average Price\": [Mean_Revenue],\n",
    "                           \" Number of Purchases\": [Item_ID],\n",
    "                           \"Total Revenue\": [Total_Revenue]})\n",
    "\n",
    "summary_df\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender\n",
       "Female                   14.49\n",
       "Male                     83.59\n",
       "Other / Non-Disclosed     1.92\n",
       "Name: Gender, dtype: float64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Percentage_of_Players = round((pymoli_df.groupby(['Gender'])['Gender'].count()/pymoli_df['Gender'].count())*100,2)\n",
    "Percentage_of_Players"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "780"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pymoli_df['Gender'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender\n",
       "Female                   113\n",
       "Male                     652\n",
       "Other / Non-Disclosed     15\n",
       "Name: Gender, dtype: int64"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Total_Count_1=pymoli_df.groupby(['Gender'])['Gender'].count()\n",
    "Total_Count_1\n",
    "#Call Dataframe and Create"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Count</th>\n",
       "      <th>Percentage of Players</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>484</td>\n",
       "      <td>62.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>81</td>\n",
       "      <td>10.38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Other / Non-Disclosed</th>\n",
       "      <td>11</td>\n",
       "      <td>1.41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Total Count  Percentage of Players\n",
       "Male                           484                  62.05\n",
       "Female                          81                  10.38\n",
       "Other / Non-Disclosed           11                   1.41"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Gender demo\n",
    "\n",
    "gender_grouped = pymoli_df[[\"SN\", \"Gender\"]]\n",
    "gender_grouped = gender_grouped.drop_duplicates()\n",
    "counts = gender_grouped[\"Gender\"].value_counts()\n",
    "\n",
    "# List of values\n",
    "total_counts = [counts[0],counts[1],counts[2]]\n",
    "Percentage = [round((counts[0]/Purchase_ID)*100,2),round((counts[1]/Purchase_ID)*100,2),round((counts[2]/Purchase_ID)*100,2)]\n",
    "\n",
    "# Creating DataFrame & setting index\n",
    "gender_demo_df = pd.DataFrame({\n",
    "    \"Total Count\": total_counts,\n",
    "    \"Percentage of Players\": Percentage\n",
    "})\n",
    "gender_demo_df.index = ([\"Male\", \"Female\", \"Other / Non-Disclosed\"])\n",
    "gender_demo_df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style>  \n",
       "<table id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966\" > \n",
       "<thead>    <tr> \n",
       "        <th class=\"blank level0\" ></th> \n",
       "        <th class=\"col_heading level0 col0\" >Purchase Count</th> \n",
       "        <th class=\"col_heading level0 col1\" >Average Purchase Price</th> \n",
       "        <th class=\"col_heading level0 col2\" >Total Purchase Value</th> \n",
       "    </tr>    <tr> \n",
       "        <th class=\"index_name level0\" >Gender</th> \n",
       "        <th class=\"blank\" ></th> \n",
       "        <th class=\"blank\" ></th> \n",
       "        <th class=\"blank\" ></th> \n",
       "    </tr></thead> \n",
       "<tbody>    <tr> \n",
       "        <th id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966level0_row0\" class=\"row_heading level0 row0\" >Male</th> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row0_col0\" class=\"data row0 col0\" >652</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row0_col1\" class=\"data row0 col1\" >$3.02</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row0_col2\" class=\"data row0 col2\" >$1967.64</td> \n",
       "    </tr>    <tr> \n",
       "        <th id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966level0_row1\" class=\"row_heading level0 row1\" >Female</th> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row1_col0\" class=\"data row1 col0\" >113</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row1_col1\" class=\"data row1 col1\" >$3.20</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row1_col2\" class=\"data row1 col2\" >$361.94</td> \n",
       "    </tr>    <tr> \n",
       "        <th id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966level0_row2\" class=\"row_heading level0 row2\" >Other / Non-Disclosed</th> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row2_col0\" class=\"data row2 col0\" >15</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row2_col1\" class=\"data row2 col1\" >$3.35</td> \n",
       "        <td id=\"T_fd6dcffe_0042_11e9_83d9_30d16be34966row2_col2\" class=\"data row2 col2\" >$50.19</td> \n",
       "    </tr></tbody> \n",
       "</table> "
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x20e72480470>"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gender_grouped = pymoli_df[[\"SN\",\"Gender\",\"Price\"]]\n",
    "counts = gender_grouped[\"Gender\"].value_counts()\n",
    "\n",
    "# Purchase counts\n",
    "purchase_counts = [counts[0],counts[1],counts[2]]\n",
    "\n",
    "gender_grouped = gender_grouped.groupby(\"Gender\")\n",
    "total_spent = gender_grouped.sum()\n",
    "total_spent\n",
    "\n",
    "# Average Purchase Price\n",
    "avg_purchase = [total_spent.iloc[1,0]/counts_g[0], total_spent.iloc[0,0]/counts_g[1], total_spent.iloc[2,0]/counts_g[2]]\n",
    "\n",
    "# Total Purchase Value\n",
    "total_purchase_value = [total_spent.iloc[1,0], total_spent.iloc[0,0], total_spent.iloc[2,0]]\n",
    "# Normalized Totals\n",
    "norm_tot = [total_spent.iloc[1,0]/counts[0], total_spent.iloc[0,0]/counts[1], total_spent.iloc[2,0]/counts[2]]\n",
    "\n",
    "# Creating DataFrame & setting index\n",
    "purchase_analysis_df = pd.DataFrame({\"Purchase Count\": purchase_counts,\n",
    "                                    \"Average Purchase Price\": avg_purchase,\n",
    "                                    \"Total Purchase Value\": total_purchase_value,\n",
    "                                    \"Gender\": [\"Male\", \"Female\", \"Other / Non-Disclosed\"]\n",
    "})\n",
    "purchase_analysis_df = purchase_analysis_df.set_index(\"Gender\")\n",
    "purchase_analysis_df = purchase_analysis_df[[\"Purchase Count\", \"Average Purchase Price\", \"Total Purchase Value\"]]\n",
    "\n",
    "# Formatting Prices\n",
    "purchase_analysis_df.style.format({\"Average Purchase Price\": \"${:.2f}\", \"Total Purchase Value\":\"${:.2f}\"})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total Count</th>\n",
       "      <th>Percent of Players</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>&lt;10</th>\n",
       "      <td>23</td>\n",
       "      <td>3.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10-14</th>\n",
       "      <td>28</td>\n",
       "      <td>4.86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15-19</th>\n",
       "      <td>136</td>\n",
       "      <td>23.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20-24</th>\n",
       "      <td>365</td>\n",
       "      <td>63.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25-29</th>\n",
       "      <td>101</td>\n",
       "      <td>17.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30-34</th>\n",
       "      <td>73</td>\n",
       "      <td>12.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35-39</th>\n",
       "      <td>41</td>\n",
       "      <td>7.12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40+</th>\n",
       "      <td>13</td>\n",
       "      <td>2.26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Total Count  Percent of Players\n",
       "<10             23                3.99\n",
       "10-14           28                4.86\n",
       "15-19          136               23.61\n",
       "20-24          365               63.37\n",
       "25-29          101               17.53\n",
       "30-34           73               12.67\n",
       "35-39           41                7.12\n",
       "40+             13                2.26"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#AGE DEMOGRAPHICS\n",
    "\n",
    "df2 = pymoli_df[[\"Purchase ID\",\"SN\",\"Age\",\"Price\"]]\n",
    "\n",
    "df2 = df2.drop_duplicates()\n",
    "\n",
    "# Count by age\n",
    "age_10 = df2[df2[\"Age\"] < 10].count()[0]\n",
    "age_14 = df2[(df2[\"Age\"] >= 10) & (df2[\"Age\"] <= 14)].count()[0]\n",
    "age_19 = df2[(df2[\"Age\"] >= 15) & (df2[\"Age\"] <= 19)].count()[0]\n",
    "age_24 = df2[(df2[\"Age\"] >= 20) & (df2[\"Age\"] <= 24)].count()[0]\n",
    "age_29 = df2[(df2[\"Age\"] >= 25) & (df2[\"Age\"] <= 29)].count()[0]\n",
    "age_34 = df2[(df2[\"Age\"] >= 30) & (df2[\"Age\"] <= 34)].count()[0]\n",
    "age_39 = df2[(df2[\"Age\"] >= 35) & (df2[\"Age\"] <= 39)].count()[0]\n",
    "age_40 = df2[df2[\"Age\"] >= 40].count()[0]\n",
    "ages = [age_10, age_14, age_19, age_24, age_29, age_34, age_39, age_40]\n",
    "\n",
    "# Percentage by age\n",
    "percent_10 = round((age_10/player_count)*100,2)\n",
    "percent_14 = round((age_14/player_count)*100,2)\n",
    "percent_19 = round((age_19/player_count)*100,2)\n",
    "percent_24 = round((age_24/player_count)*100,2)\n",
    "percent_29 = round((age_29/player_count)*100,2)\n",
    "percent_34 = round((age_34/player_count)*100,2)\n",
    "percent_39 = round((age_39/player_count)*100,2)\n",
    "percent_40 = round((age_40/player_count)*100,2)\n",
    "percents_a = [percent_10, percent_14, percent_19, percent_24, percent_29, percent_34, percent_39, percent_40]\n",
    "\n",
    "# Creating the dictionary\n",
    "age_demo = {\n",
    "        \"Total Count\": ages,\n",
    "        \"Percent of Players\": percents_a\n",
    "       \n",
    "    }\n",
    "    \n",
    "# DF\n",
    "age_demo_df = pd.DataFrame(age_demo)\n",
    "age_demo_df.index = ([\"<10\", \"10-14\", \"15-19\", \"20-24\", \"25-29\", \"30-34\", \"35-39\", \"40+\"])\n",
    "age_demo_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
