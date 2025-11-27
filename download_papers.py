import os
import requests

# Create directory
output_folder = "ANPR_Papers_PDFs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of papers (Same list as before)
papers = {
    "1_Deep_Learning_Survey_Vehicle_Detection": "https://www.ijstr.org/final-print/dec2019/A-Survey-On-Deep-Learning-Approaches-For-Vehicle-And-Number-Plate-Detection.pdf",
    "2_Vehicle_Number_Plate_Detection_Review": "https://www.researchgate.net/publication/350488454_Vehicle_Number_Plate_Detection_and_Recognition_Techniques_A_Review",
    "3_ANPR_System_Survey": "https://www.researchgate.net/publication/236888959_Automatic_Number_Plate_Recognition_System_ANPR_A_Survey",
    "4_Automated_License_Plate_Detection_Deep_Learning": "https://www.researchgate.net/publication/367301980_Automated_License_Plate_Detection_and_Recognition_Using_Deep_Learning",
    "5_Survey_Automatic_Number_Plate_Detection": "https://www.ijsrd.com/articles/IJSRDV8I20491.pdf",
    "6_Detailed_Survey_ANPR_Advancements": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8123416/pdf/main.pdf",  # Attempted fix for PMC
    "7_ANPR_In_Smart_Cities_Review": "https://doi.org/10.1016/j.cities.2022.103833",
    "8_Multi_Stage_Deep_Learning_ANPR": "https://www.mdpi.com/1424-8220/23/4/2120/pdf", # Attempted fix for MDPI
    "9_End_To_End_ANPR_Indian_Datasets": "https://arxiv.org/abs/2207.06657",
    "10_ANPR_Relevance_Vehicle_Theft": "https://www.mdpi.com/2673-4591/59/1/185/pdf",
    "11_Efficient_Approach_Number_Plate_Extraction": "https://www.researchgate.net/publication/262843164_An_Efficient_Approach_for_Number_Plate_Extraction_from_Vehicles_Image_under_Image_Processing",
    "12_ANPR_Histogram_Equalization": "https://ieeexplore.ieee.org/document/10568583/",
    "13_Efficient_Technique_Indian_Vehicles_SVM": "https://www.ijrte.org/wp-content/uploads/papers/v8i3/C4161098319.pdf",
    "14_ANPR_Random_Forest_Classifier": "https://arxiv.org/abs/2303.14856",
    "15_License_Plate_Detection_CNN": "https://ieeexplore.ieee.org/document/8322837/",
    "16_CNN_Based_Approach_ANPR_Wild": "https://www.researchgate.net/publication/332813502_A_CNN-Based_Approach_for_Automatic_License_Plate_Recognition_in_the_Wild",
    "17_Knowledge_Distillation_Fast_CNN": "https://ieeexplore.ieee.org/document/10309208/",
    "18_Intelligent_System_ANPR_CNNs": "https://www.mdpi.com/2227-7080/9/1/9/pdf",
    "19_ANPR_YOLOv3_CNN": "https://arxiv.org/abs/2211.05229",
    "20_Efficient_Real_Time_ANPR_Gas_Stations": "https://colab.ws/articles/10.1007%2F978-981-16-0730-1_20",
    "21_License_Plate_Detection_CNN_DOE": "https://www.researchgate.net/publication/358839918_License_Plate_Detection_Using_Convolutional_Neural_Network_-_Back_to_The_Basic_with_Design_of_Experiments",
    "22_Study_Car_Plate_Recognition_YOLOv4": "https://ieeexplore.ieee.org/document/10730590/",
    "23_Novel_Memory_Time_Efficient_ALPR_YOLOv5": "https://www.researchgate.net/publication/362042453_A_Novel_Memory_and_Time-Efficient_ALPR_System_Based_on_YOLOv5",
    "24_Real_Automatic_Number_Plate_Yolo": "https://jscer.org/wp-content/uploads/2024/2024-Volume%207-Issue%207/Real%20Automatic%20Number%20Plate%20Image%20Detection%20With.pdf",
    "25_Enhanced_YOLOv8_ANPR": "https://www.mdpi.com/2227-7080/12/9/164/pdf",
    "26_ANPR_YOLO_World": "https://colab.ws/articles/10.1016%2Fj.compeleceng.2024.109646",
    "27_ANPRSmaC_Smart_City": "https://ieeexplore.ieee.org/document/10830363/",
    "28_ANPR_YOLOv8_Model": "https://www.researchgate.net/publication/391200581_Automatic_Number_Plate_Recognition_Using_YOLOv8_Model",
    "29_Weather_Adaptive_CNN_Framework": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11644901/pdf/main.pdf",
    "30_Deep_Learning_Segmentation_Free_LPR": "https://arxiv.org/abs/1912.02441",
    "31_Systematic_Review_OCR_ANPR": "https://ieeexplore.ieee.org/document/10131688/",
    "32_Real_Time_APR_OCR_WSN": "https://www.mdpi.com/1424-8220/20/1/55/pdf",
    "33_Real_Time_OCR_FPGA_ANPR": "https://www.researchgate.net/publication/264563872_Real-time_optical_character_recognition_on_field_programmable_gate_array_for_automatic_number_plate_recognition_system",
    "34_LPRNet_Deep_Neural_Networks": "https://arxiv.org/abs/1806.10447",
    "35_Deep_Learning_Super_Resolution_LPR": "https://www.mdpi.com/2227-7390/13/10/1673/pdf",
    "36_Open_Data_Moroccan_License_Plates": "https://arxiv.org/abs/2104.08244",
    "37_Chaurah_Smart_Parking_Raspberry_Pi": "https://arxiv.org/abs/2312.16894",
    "38_License_Plate_Detection_Smart_Parking": "https://www.springerprofessional.de/en/license-plate-detection-for-smart-parking-management/18784256",
    "39_Automatic_Traffic_Red_Light_Violation_AI": "https://www.iieta.org/download/file/fid/69639",
    "40_Real_Time_Traffic_Density_Red_Light": "https://ieeexplore.ieee.org/document/10169241/",
    "41_Automatic_Monitoring_Traffic_Violation": "https://www.researchgate.net/publication/355281701_Application_of_Artificial_Neural_Network_to_ANPR_An_Overview",
    "42_Smart_Traffic_Control_Fog_Devices": "https://www.researchgate.net/publication/351369171_Smart_traffic_control_Identifying_driving-violations_using_fog_devices_with_vehicular_cameras_in_smart_cities",
    "43_Automatic_E_Challan_YOLO_OpenCV": "https://ijsret.com/wp-content/uploads/2024/11/IJSRET_V10_issue6_569.pdf",
    "44_Traffic_Violation_Detection_Deep_Learning": "https://www.researchgate.net/publication/391473338_Traffic_Violation_Detection_Using_Deep_Learning",
    "45_TVD_MRDL_MapReduce_Deep_Learning": "https://doi.org/10.1007/s11042-020-09714-8",
    "46_Real_Time_Helmet_Detection_Number_Plate": "https://www.researchgate.net/publication/379542926_Real-Time_Helmet_Detection_and_Number_Plate_Extraction_Using_Computer_Vision",
    "47_Efficient_Intelligent_Compliance_Traffic": "https://ieeexplore.ieee.org/document/10581025/",
    "48_YoloV8_Traffic_Violation_Intelligent_Signal": "https://ijarcce.com/wp-content/uploads/2025/05/IJARCCE.2025.14584.pdf",
    "49_Deep_Learning_Traffic_Violation_PaddleOCR": "https://ieeexplore.ieee.org/document/11035399/",
    "50_Helmet_Number_Plate_DetectNet_YOLOv8": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1582257/full",
    "51_ANPR_System_Machine_Learning_Techniques": "https://ieeexplore.ieee.org/document/10739064/",
    "52_ANPR_Small_Moped_Plates": "https://tugraz.elsevierpure.com/en/publications/automatic-number-plate-detection-and-recognition-system-for-small",
    "53_Automatic_Vehicle_Number_Plate_ML": "https://www.researchgate.net/publication/349629053_Automatic_Vehicle_Number_Plate_Recognition_System_Using_Machine_Learning"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

skipped_links = []
downloaded_count = 0

print(f"Starting Smart Download Process for {len(papers)} papers...")
print("-" * 50)

for title, url in papers.items():
    
    # 1. FIX ARXIV LINKS AUTOMATICALLY
    if "arxiv.org/abs/" in url:
        print(f"🔄 Converting ArXiv Abstract to PDF link for: {title}")
        url = url.replace("abs/", "pdf/") + ".pdf"
        
    try:
        # Request the URL
        print(f"🔍 Checking: {title}...")
        response = requests.get(url, headers=headers, timeout=15, stream=True)
        
        # 2. CHECK CONTENT TYPE (MUST BE PDF)
        content_type = response.headers.get('Content-Type', '').lower()
        
        if 'application/pdf' in content_type:
            filename = f"{output_folder}/{title}.pdf"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✅ DOWNLOADED: {filename}\n")
            downloaded_count += 1
        else:
            # It's an HTML page (Landing page)
            print(f"⚠️ SKIPPED (Not a direct PDF): {title}\n")
            skipped_links.append(f"{title}: {url}")
            
    except Exception as e:
        print(f"❌ ERROR: {title} - {e}\n")
        skipped_links.append(f"{title}: {url}")

# Save skipped links to a file for manual checking
if skipped_links:
    with open("manual_download_list.txt", "w") as f:
        f.write("These links are landing pages or paywalled. You must open them manually to download the PDF:\n\n")
        for line in skipped_links:
            f.write(line + "\n")

print("-" * 50)
print(f"🎉 Process Complete!")
print(f"📥 Total PDFs Downloaded: {downloaded_count}")
print(f"⏭️  Total Skipped: {len(skipped_links)}")
print("📄 Check 'manual_download_list.txt' for the links you need to open manually.")