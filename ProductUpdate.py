"""
Product Updating Program
Editor: Corey Berther
Company: DSM
Client: VC Fruits
Date: 29/3/2024

"""

import pandas as pd

__name__ = "__main__"

def conversion(csv1: str, csv2: str) -> None:
    """
    This is the main algorithm that
    actually converts the data of the
    clients updated csv file to the
    actual shopify csv file
    """
    
    #template new product dictionary
    #when adding a new product, must change name, category and price
    newproduct = {
        'Handle': '',
        'Title': 'NAME',
        'Body (HTML)': '',
        'Vendor': 'VC Fruit Market',
        'Product Category': 'CATEGORY',
        'Type': '',
        'Tags': 'TRUE',
        'Published': 'Title',
        'Option1 Name': 'Default Title',
        'Option1 Value': '',
        'Option2 Name': '',
        'Option2 Value': '',
        'Option3 Name': '',
        'Option3 Value': '',
        'Variant SKU': '1',
        'Variant Grams': 'PRICE',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '100',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '0.00',
        'Variant Compare At Price': '',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Variant Barcode': '',
        'Image Src': 'https://vcfruitmarket.com.au/cdn/shop/files/vc_fruit_market_6_x90@2x.png?v=1708345597',
        'Image Position': '1',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': '',
        'SEO Description': '',
        'Google Shopping / Google Product Category': '',
        'Google Shopping / Gender': '',
        'Google Shopping / Age Group': '',
        'Google Shopping / MPN': '',
        'Google Shopping / Condition': '',
        'Google Shopping / Custom Product': '',
        'Google Shopping / Custom Label 0': '',
        'Google Shopping / Custom Label 1': '',
        'Google Shopping / Custom Label 2': '',
        'Google Shopping / Custom Label 3': '',
        'Google Shopping / Custom Label 4': '',
        'Variant Image': '',
        'Variant Weight Unit': 'kg',
        'Variant Tax Code': '',
        'Cost per item': '',
        'Included / Australia': 'TRUE',
        'Price / Australia': '',
        'Compare At Price / Australia': '',
        'Included / International': 'TRUE',
        'Price / International': '',
        'Compare At Price / International': '',
        'Status': 'active'
    }
    
    print("Reading csv files...")
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    print("Adding Products...")
    # Iterate through each row
    for index1, row1 in df1.iterrows():
        name = row1['name']
        category = row1['category']
        
        #fix typo in csv
        if category == "Gocery GST":
            category = "Grocery GST"
 
        #deactive product
        if row1['status'] == "DEACTIVE":
            for index2, row2 in df2.iterrows():
                if name == row2['Title']:
                    df2.at[index2, 'Status'] = "draft"
                    df2.at[index2, 'Product Category'] = category
                    
            
        #add new product
        if row1['NEW PRODUCT'] == "NEW PRODUCT":
            np = newproduct
            
            np['Title'] = name
            np['Product Category'] = category
            np['Variant Price'] = row1['new price']
            df2.loc[len(df2)] = np

        #change price of product
        if row1['new price'] != None and row1['NEW PRODUCT'] != "NEW PRODUCT" :
            for index2, row2 in df2.iterrows():
                if name == row2['Title']:
                    df2.at[index2, 'Variant Price'] = row1['new price']
                    df2.at[index2, 'Product Category'] = category
                    
        
            
            

    print("Finalising write to csv...")
    df2.to_csv(csv2, index=False)
    print("Done!")

def main():
    """
    Main function
    """
    while True:
        csv1 = str(input("Client Updated Products CSV Path: "))
        csv2 = str(input("Current Shopify Products CSV Path: "))
        
        conversion(csv1,csv2)
        
        again = input("Again? (y/n): ")
        if again == "n":
            break
        
        
if __name__ == "__main__":
    main()
    
