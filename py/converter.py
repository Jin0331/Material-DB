import os
import json
import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def blood_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/blood"
    file_name = timeStamped("blood.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Gooipchu", "Patient_defualt", "Patient_smoking", "Patient_alcohol", "Treatment_history", "Singel_cell_seperation_date",
                          "Cell_population", "Cytokine_profile", "In_vitro_coculture_with", "Tested_drug"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Gooipchu.append({"Gooknae":line[4], "Haeoe":line[5]})
        Patient_defualt.append({"Gender":line[15], "Age":line[16], "Height":line[17], "Weight":line[18]})
        Patient_smoking.append({"Status":line[19], "Cigarettes_Day":line[20], "Duration":line[21]})
        Patient_alcohol.append({"Status":line[22], "Drinks_Day":line[23], "Duration":line[24]})
        Treatment_history.append({"Prior_Treatment":line[25], "Erbitux_Responder":line[26], "Erbitux_Non_Responder":line[27], 
                                 "Treatment_History1_Responder":line[28], "Treatment_History1_Non_Responder":line[29]})
        Singel_cell_seperation_date.append({"Date":line[30], "Manager":line[31]})
        Cell_population.append({"Information":line[32], "Manager":line[33]})
        Cytokine_profile.append({"Information":line[34], "Manager":line[35]})
        In_vitro_coculture_with.append({"Information":line[36], "Manager":line[37]})
        Tested_drug.append({"Information":line[38], "Manager":line[39], "Patient_information":line[40]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gumche_bungo":line[3], 
                     "Gooipchu":Gooipchu, "Ethnicity":line[6], "Tissue":line[7], "Ipgo_hyngtae":line[8],
                     "Insooja":line[9], "Ipgo_Date":line[10], "Location":line[11], "Cancer":line[12],"Tumor_Grade":line[13],
                     "Tumor_Stage":line[14], "Patient_defualt":Patient_defualt, "Patient_smoking":Patient_smoking, 
                     "Patient_alchohol":Patient_alcohol, "Treatment_history" : Treatment_history, 
                     "Singel_cell_seperation_date":Singel_cell_seperation_date, "Cell_population":Cell_population, 
                     "Cytokine_profile":Cytokine_profile, "In_vitro_coculture_with":In_vitro_coculture_with, "Tested_drug":Tested_drug,
                     "New1":line[41], "New2":line[42], "New3":line[43], "New4":line[44], "New5":line[45]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting


def blood_result_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/blood_result"
    file_name = timeStamped("blood_result.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Experimental_Information"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Experimental_Information.append({"image_path":line[4], "Meterial":line[5], "Method":line[6],
                                "Condition":line[7], "Experimental_content":line[8], "Result":line[9], "Manager":line[10], "Date":line[11]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gumche_bungo":line[3], 
                     "Experimental_Information":Experimental_Information})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def pdx_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/pdx"
    file_name = timeStamped("pdx.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Gooipchu", "Patient_defualt", "Patient_smoking", "Patient_alcohol", "Treatment_history", "Experimental_animals",
                          "Characterization"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Gooipchu.append({"Gooknae":line[4], "Haeoe":line[5]})
        Patient_defualt.append({"Gender":line[15], "Age":line[16], "Height":line[17], "Weight":line[18]})
        Patient_smoking.append({"Status":line[19], "Cigarettes_Day":line[20], "Duration":line[21]})
        Patient_alcohol.append({"Status":line[22], "Drinks_Day":line[23], "Duration":line[24]})
        Treatment_history.append({"Prior_Treatment":line[25], "Drug":line[26], "Drug2":line[27]})
        Experimental_animals.append({"Mouse_Type":line[29], "Gooipchu":line[30]})
        Characterization.append({"Chemoresistance_status":line[31], "Mutation_status":line[32], "RON_Genotype":line[33],
                                "IGSF1_Genotype":line[34], "P34_Genotype":line[35]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gumche_bungo":line[3], 
                     "Gooipchu":Gooipchu, "Ethnicity":line[6], "Tissue":line[7], "Disease":line[8], "Ipgo_hyngtae":line[9],
                     "Insooja":line[10], "Ipgo_Date":line[11], "Location":line[12], "Tumor_Grade":line[13],
                     "Tumor_Stage":line[14], "Patient_defualt":Patient_defualt, "Patient_smoking":Patient_smoking, 
                     "Patient_alchohol":Patient_alcohol, "Treatment_history" : Treatment_history,
                     "Histological_Description":line[28], "Experimental_animals":Experimental_animals,
                     "Characterization":Characterization, "New1":line[36], "New2":line[37], "New3":line[38], "New4":line[39], "New5":line[40], "New6":line[41], 
                     "New7":line[42], "New8":line[43]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting


def pdx_result_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/pdx_result"
    file_name = timeStamped("pdx_result.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Experimental_Information"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Experimental_Information.append({"image_path":line[10], "Experimental_tissue":line[11], "Passage":line[12],
                                "Media":line[13], "Transplantation_point":line[14], "Administration_point":line[15],
                                "Transplantation_Administration_duration":line[16], "Issue":line[17], "Experimental_info":line[18],
                                "Experimental_result":line[19], "Manager":line[20]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gumche_bungo":line[3], 
                     "Tissue_site":line[4], "Cancer":line[5], "Tumor_Grade":line[6], "Tumor_Stage":line[7], "Treatment_History":line[8],
                     "Drug_resistant":line[9], "Experimental_Information":Experimental_Information})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def ff_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/ff"
    file_name = timeStamped("ff.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Gooipchu", "Subdivide_Tissue", "Patient_defualt", "Patient_smoking", "Patient_alcohol", "Patient_surgery",
                           "Treatment_history", "RT_PCR", "WB_Experimental"
                          ]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Gooipchu.append({"Gooknae":line[3], "Haeoe":line[4]})
        Subdivide_Tissue.append({"Subdivide_Date":line[15], "Subdivide_count":line[16]})
        Patient_defualt.append({"Gender":line[18], "Age":line[19], "Height":line[20], "Weight":line[21]})
        Patient_smoking.append({"Status":line[22], "Cigarettes_Day":line[23], "Duration":line[24]})
        Patient_alcohol.append({"Status":line[25], "Drinks_Day":line[26], "Duration":line[27]})
        Patient_surgery.append({"Date_of_surgery":line[28], "Metastases":line[29]})
        Treatment_history.append({"Prior_Treatment":line[30], "Drug_Response":line[31]})
        RT_PCR.append({"RON":line[35], "KRAS":line[36], "BRAF":line[37], "EGFR":line[38], "IGSF1":line[39], "RT_PCR1":line[40],
                      "RT_PCR2":line[41], "RT_PCR3":line[42], "RT_PCR4":line[43], "RT_PCR5":line[44],  "RT_PCR6":line[45]})
        WB_Experimental.append({"WB_Experimental1":line[46], "WB_Experimental2":line[47], "WB_Experimental3":line[48], 
                               "WB_Experimental4":line[49], "WB_Experimental5":line[50], "WB_Experimental6":line[51]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gooipchu":Gooipchu,
                                 "Ethnicity":line[5], "Tissue_site":line[6], "Matrix":line[7], "Insooja":line[8],
                                 "Ipgo_Date":line[9], "Tumor_Grade":line[10], "Tumor_Stage":line[11], "Tumor_contents":line[12],
                                 "Tumor_size":line[13], "Tumor_Weight":line[14], "Subdivide_Tissue":Subdivide_Tissue, "Location":line[17],
                                 "Patient_defualt":Patient_defualt, "Patient_smoking":Patient_smoking, "Patient_alcohol":Patient_alcohol,
                                 "Patient_surgery":Patient_surgery, "Treatment_history":Treatment_history, "Histological Description":line[32],
                                 "TNM_Staging":line[33], "Microsatellite instability":line[34], "RT_PCR":RT_PCR, "WB_Experimental":WB_Experimental,
                                 "New1":line[52], "New2":line[53], "New3":line[54], "New4":line[55], "New5":line[56], "New6":line[57], "New7":line[58]
                                })  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def ff_result_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/ff_result"
    file_name = timeStamped("ff_result.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = [
                            "Treatment_history", "RT_PCR", "WB_Experimental"
                          ]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Treatment_history.append({"Prior_Treatment":line[6], "Drug_Response":line[7]})
        RT_PCR.append({"RON":line[8], "KRAS":line[9], "BRAF":line[10], "EGFR":line[11], "IGSF1":line[12], "RT_PCR1":line[13],
                      "RT_PCR2":line[14], "RT_PCR3":line[15], "RT_PCR4":line[16], "RT_PCR5":line[17], "RT_PCR6":line[18],
                      "RT_PCR7":line[19], "RT_PCR8":line[20]})
        WB_Experimental.append({"RON":line[21], "BRAF":line[22], "EGFR":line[23], "WB_Experimental1":line[24], "WB_Experimental2":line[25],
                               "WB_Experimental3":line[26], "WB_Experimental4":line[27], "WB_Experimental5":line[28], "WB_Experimental6":line[29], 
                               "WB_Experimental7":line[30], "WB_Experimental8":line[31], "WB_Experimental9":line[32]})
        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Tissue_site":line[3], "Tumor_Grade":line[4], 
                                 "Tumor_Stage":line[5], "Treatment_history":Treatment_history, "RT_PCR":RT_PCR, "WB_Experimental":WB_Experimental
                                })  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def ffpe_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/ffpe"
    file_name = timeStamped("ffpe.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Gooipchu", "Subdivide_Tissue", "Patient_defualt", "Patient_smoking", "Patient_alcohol", "IHC_result"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Gooipchu.append({"Gooknae":line[3], "Haeoe":line[4]})
        Patient_defualt.append({"Gender":line[14], "Age":line[15], "Height":line[16], "Weight":line[17]})
        Patient_smoking.append({"Status":line[18], "Cigarettes_Day":line[19], "Duration":line[20]})
        Patient_alcohol.append({"Status":line[21], "Drinks_Day":line[22], "Duration":line[23]})
        IHC_result.append({"p53":line[24], "p34":line[25], "MDM2":line[26], "pRON":line[27], "RON":line[28], "MSP":line[29], "cmyc":line[30],
                          "PDL1":line[31], "IGSF1":line[32], "New1":line[33], "New2":line[34], "New3":line[35],"New4":line[36], "New5":line[37],
                          "New6":line[38], "New7":line[39], "New8":line[40], "New9":line[41], "New10":line[42], "New11":line[43], "New12":line[44],
                          "New13":line[45], "New14":line[46], "New15":line[47], "New16":line[48], "New17":line[49], "New18":line[50], "New19":line[51],
                          "New20":line[52], "New21":line[53]})

        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Gooipchu":Gooipchu,
                                 "Ethnicity":line[5], "Tissue_site":line[6], "Ipgo_hyngtae":line[7], "Insooja":line[8],
                                 "Ipgo_Date":line[9], "Location":line[10], "Cancer":line[11], "Tumor_Grade":line[12], "Tumor_Stage":line[13],
                                 "Patient_defualt":Patient_defualt, "Patient_smoking":Patient_smoking, "Patient_alcohol":Patient_alcohol,
                                 "IHC_result":IHC_result})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def ffpe_result_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/ffpe_result"
    file_name = timeStamped("ffpe_result.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = [
                            "WB_Experimental"
                          ]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        WB_Experimental.append({"Image":line[7], "Target":line[8], "Antibody":line[9], "Score":line[10], "Experimental_information":line[11],
                               "Experimental_result":line[12], "manager":line[13]})
        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "SampleID":line[1], "FF_ID":line[2], "Tissue_site":line[3], "Cancer":line[4],"Tumor_Grade":line[5], 
                                 "Tumor_Stage":line[6], "WB_Experimental":WB_Experimental
                                })  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting



def drug_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/drug"
    file_name = timeStamped("drug.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "Drug_Name":line[1], "Manufacturer":line[2], "Volume":line[3], 
                         "Target":line[4], "Cat":line[5], "Gooipchu":line[6], "Location":line[7], "Manager":line[8], "etc":line[9],
                         "Data_sheet":line[10], "New1":line[11], "New2":line[12], "New3":line[13], "New4":line[14], "New5":line[15], "New6":line[16]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def antibody_WB_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/antibody_wb"
    file_name = timeStamped("antibody_wb.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"No":line[0], "WMB_NO":line[1], "Antibody":line[2], "Cat_No":line[3], "Lot_No":line[4], 
                         "Conc":line[5], "Host":line[6], "Species_Reactivity":line[7], "Application":line[8], "Use_Titer":line[9], 
                         "Blocking Buffer":line[10], "Protein_size":line[11], "Vial":line[12], "Ipgo_date":line[13], "Location":line[14],
                         "Manager":line[15], "Manufacturer":line[16], "etc":line[17], "New1":line[18], "New2":line[19], "New3":line[20],
                         "New4":line[21], "New5":line[22], "New6":line[23], "New7":line[24], "New8":line[25]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def antibody_IHC_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/antibody_ihc"
    file_name = timeStamped("antibody_ihc.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"No":line[0], "WMB_NO":line[1], "Antibody":line[2], "Cat_No":line[3], "Lot_No":line[4], 
                         "Conc":line[5], "Host":line[6], "Species_Reactivity":line[7], "Application":line[8], "Use_Titer":line[9], 
                         "Blocking Buffer":line[10], "Protein_size":line[11], "Vial":line[12], "Ipgo_date":line[13], "Location":line[14],
                         "Manager":line[15], "Manufacturer":line[16], "etc":line[17], "New1":line[18], "New2":line[19], "New3":line[20],
                         "New4":line[21], "New5":line[22], "New6":line[23], "New7":line[24], "New8":line[25]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def antibody_FACS_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/antibody_facs"
    file_name = timeStamped("antibody_facs.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"Antibody":line[0], "Cat_No":line[1], "Host":line[2], "Species_Reactivity":line[3], "Application":line[4],
                                "Location":line[5], "Manager":line[6], "Manufacturer":line[7], "etc":line[8], "New1":line[9], "New2":line[10],
                                "New3":line[11], "New4":line[12], "New5":line[13]})        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting



def protein_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/protein"
    file_name = timeStamped("protein.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"Project":line[0], "WMB_NO":line[1], "Reagent_name":line[2], "Manufacturer":line[3], "Cat_No":line[4], 
                         "Lot_No":line[5], "Leftover":line[6], "Location":line[7], "Data_sheet":line[8], "New1":line[9], "New2":line[10], "New3":line[11],
                         "New4":line[12], "New5":line[13], "New6":line[14], "New7":line[15], "New8":line[16], "New9":line[17], "New10":line[18]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def shsirna_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/shsirna"
    file_name = timeStamped("shsirna.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")
        
        # Inserting Data
        total_converting.append({"Project":line[0], "WMB_NO":line[1], "Name":line[2], "Target_Gene":line[3], "Species":line[4], 
                         "Type":line[5], "Concentration":line[6], "Sequence":line[7], "Manufacturer":line[8], "Stock_vial_ipgo":line[9],
                         "Stock_vial_liftover":line[10], "Stock_vial_location":line[11], "Subdivide_vial_liftover":line[12], "Location":line[13],
                         "Manager":line[14], "Data_sheet":line[15], "New1":line[16], "New2":line[17], "New3":line[18], "New4":line[19], 
                         "New5":line[20], "New6":line[21], "New7":line[22], "New8":line[23], "New9":line[24], "New10":line[25]})  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting

def celline_to_mongo(path, base_path):
    # backup file write
    save_path = base_path + "/backup/celline"
    file_name = timeStamped("celline.json")
    date_join = os.path.join(save_path, file_name)
    
    # txt to json(list or tuple)
    total_converting = list()

    f = open(path, "r", encoding="UTF-8")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent:
        line = line.split("\t")

        # tuple list
        # assiagn empty list
        empty_list_name = ["Characterization", "RT_PCR", "WB"]
        for name in empty_list_name:
            exec("%s = list()" %(name), globals())

        # each filed to tuple
        Characterization.append({"Chemoresistance_status":line[6], "Mutation_status":line[7], "RON_Genotype":line[8], "IGSF1 Genotype":line[9],
                                "P34_Genotype":line[10]})
        RT_PCR.append({"RON":line[16], "KRAS":line[17], "BRAF":line[18], "EGFR":line[19]})
        WB.append({"RON":line[20], "BRAF":line[21], "EGFR":line[22]})
        
        # Inserting Data
        total_converting.append({"WMB_NO":line[0], "Celline":line[1], "Tissue":line[2], "Organism":line[3], "Disease":line[4], 
                                 "Picture":line[5], "Characterization":Characterization, "Media_Condition":line[11], "GROWTH_PATTERN":line[12],
                                 "Ratio_Period":line[13], "Purchase":line[14], "Issue":line[15], "RT_PCR":RT_PCR, "WB":WB, "New1":line[23],
                                 "New2":line[24], "New3":line[25], "New4":line[26], "New5":line[27], "New6":line[28], "New7":line[29], 
                                 "New8":line[30], "New9":line[31], "New10":line[32]
                                })  
        
    with open(date_join, 'w', encoding="UTF-8") as file:
        file.write((json.dumps(total_converting, indent=4, sort_keys= False, ensure_ascii=False)))
    
    return total_converting