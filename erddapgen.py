import os
import subprocess
import time

def main():
    """
    This function asks the user if they want to generate a private or public dataset (currently we only have public datasets on this ERDDAP) -- commented out due to added complexity and lack of use.
    Next, it runs the genPublic() function to print the lists of all dataset categories and modify the requested file.
    Then, it runs mv to move the file to the right place, removes datasets.xml, recreates it, and exits.  
    Parameters: none
    Returns: nothing
    """

    #get whether we want public or private dataset
    #print "Please select from one of the following options:"
    #print "pub: public     |    pri: private" 
    #pubOrPri = raw_input()

    #error checking
    #while not (pubOrPri=="pub" or pubOrPri=="pri"):
    #    print("error: invalid input. Please enter \"pri\" or \"pub\"")
    #    answer=raw_input()
    pubOrPri = "pub"
    if pubOrPri=="pub":
        #print the datasets and their numbers
        printPublicDatasets()
        #generate the datasets
        filename = genPublic()
        fullFilename = "/usr/local/tomcat2/content/erddap/" + filename + ".xml"
        print fullFilename    
        #move the file to the right location and remove datasets.xml, then replace it with the new datasets.xml
        subprocess.call(["mv", "./temp/EDDGridFromThreddsCatalog.xml", fullFilename])
        subprocess.call(["rm", "/usr/local/tomcat2/content/erddap/datasets.xml"])
        os.chdir("/usr/local/tomcat2/content/erddap/")
        f = open("datasets.xml","w")
        subprocess.call(["cat start.xml datasets*_*.xml end.xml > datasets.xml"],shell=True)

    if pubOrPri=="pri":
        print "Private Datasets are not yet supported in our ERDDAP"
     #  printPrivateDatasets()
     #  filename = genPrivate()
     #  fullFilename="/usr/local/tomcat2/content/erddap/" + filename + ".xml"
     #  print fullFilename 


        
  
def genPublic():
    """
    This does all the work of generating the new dataset xml file. It gets a selection from the user, runs the
    GenerateDatasetsXml.sh program with right inputs, and cleans up the generated file.
    Parameters: None
    Returns: The name of the generated file
    """


    selection = raw_input("Select from the above: ")
    numDatasets = 46
    try:
        if int(selection) > numDatasets or int(selection) < 1:
            print "Not in range. Range is currently 1 to {0}, inclusive.".format(numDatasets)
            exit()
    except:
        print "Invalid input. Quitting."
        exit()

    os.chdir("/usr/local/tomcat2/webapps/erddap/WEB-INF")

    #the actual command we pass to GenerateDatasetsXml.sh is created in these lines
    command = "/usr/local/tomcat2/webapps/erddap/WEB-INF/GenerateDatasetsXml.sh"
    option1 = "EDDGridFromThreddsCatalog"
    option2 = "http://apdrc.soest.hawaii.edu/thredds/catalog/las/catalog.xml"
#	different URL for OfES
    if selection == "44" or selection == "45":
        option2="http://apdrc.soest.hawaii.edu/thredds/catalog/las_ofes/catalog.xml"
    option3 = "\"\""

    if selection=="1":
        regex=".*_Argo_Products_.*"
        filename="datasets1_Argo_Products"

    elif selection=="2":
        regex=".*_CFSv2_.*"
        filename="datasets2_CFSv2"

    elif selection=="3":
        regex=".*_CMIP5_.*"
        filename="datasets3_CMIP5"

    elif selection=="4":
        regex=".*_CSIRO_Atlas_.*"
        filename="datasets4_CSIRO_Atlas"

    elif selection=="5":
        regex=".*_CliPAS_.*"
        filename="datasets5_CLiPAS"

    elif selection=="6":
        regex=".*_CDASK1.4_.*"
        filename="datasets6_dask14"

    elif selection=="7":
        regex=".*_ECCO2_.*"
        filename="datasets7_ECCO2"

    elif selection=="8":
        regex=".*_ERA-40_.*"
        filename="datasets8_ERA-40"

    elif selection=="9":
        regex=".*_ERA75deg_.*"
        filename="datasets9_ERA75"

    elif selection=="10":
        regex=".*_FRA-JCOPE2_.*"
        filename="datasets10_FRA-JCOPE2"

    elif selection=="11":
        regex=".*_GAME_.*"
        filename="datasets11_GAME"

    elif selection=="12":
        regex=".*_GFDL_.*"
        filename="datasets12_GFDL"

    elif selection=="13":
        regex=".*_HadSST_.*"
        filename="datasets13_HadSST"

    elif selection=="14":
        regex=".*_ISVHE_.*"
        filename="datasets14_ISVHE"

    elif selection=="15":
        regex=".*_Interpolated_precipitation_.*"
        filename="datasets15_Interpolated_precipitation"

    elif selection=="16":
        regex=".*_J-OFURO2_.*"
        filename="datasets16_J-OFURO"

    elif selection=="17":
        regex=".*_KYUSHU_.*"
        filename="datasets17_KYUSHU"

    elif selection=="18":
        regex=".*_Model_output_.*"
        filename="datasets18_Model_output"

    elif selection=="19":
        regex=".*_NCOM_.*"
        filename="datasets19_NCOM"

    elif selection=="20":
        regex=".*_NLOM_.*"
        filename="datasets20_NLOM"

    elif selection=="21":
        print "This appears to be no longer in use. If I'm wrong, please continue."
        regex=".*_NLOM_32_.*"
        filename="datasets21_NLOM_32"

    elif selection=="22":
        regex=".*_NOAA_SST_.*"
        filename="datasets22_NOAA_SST"

    elif selection=="23":
        regex=".*_Ocean_Climatology_.*"
        filename="datasets23_Ocean_Climatology"

    elif selection=="24":
        regex=".*_PODAAC_.*"
        filename="datasets24_PODAAC"

    elif selection=="25":
        regex=".*_PRIDE_.*"
        filename="datasets25_PRIDE"

    elif selection=="26":
        regex=".*_Paleoclimate_modeling_.*"
        filename="datasets26_Paleoclimate_modeling"

    elif selection=="27":
        regex=".*_Reanalysis_Data_.*"
        filename="datasets27_Reanalysis_Data"

    elif selection=="28":
        regex=".*_SCUD_.*"
        filename="datasets28_SCUD"

    elif selection=="29":
        regex=".*_SOCAT_.*"
        filename="datasets29_SOCAT"

    elif selection=="30":
        regex=".*_SODA_.*"
        filename="datasets30_SODA"

    elif selection=="31":
        regex=".*_Tohoku_.*"
        filename="datasets31_Tohoku"

    elif selection=="32":
        regex=".*_Typhoon_Reanalysis_.*"
        filename="datasets32_Typhoon_Reanalysis"

    elif selection=="33":
        regex=".*_WASWind_.*"
        filename="datasets33_WASWind"

    elif selection=="34":
        regex=".*_WHOI_OAFlux_.*"
        filename="datasets34_WHOI_OAFlux"

    elif selection=="35":
        regex=".*_WOA_.*"
        filename="datasets35_WOA"

    elif selection=="36":
        regex=".*_bimodal_ISO_index_.*"
        filename="datasets36_bimodal_ISO_index"

    elif selection=="37":
        regex=".*_hydrobase_.*"
        filename="datasets37_hydrobase"

    elif selection=="38":
        regex=".*_hydrological_data_.*"
        filename="datasets38_hydrological_data"

    elif selection=="39":
        regex=".*_iCOADS_.*"
        filename="datasets39_iCOADS"

    elif selection=="40":
        regex=".*_satellite_product_.*"
        filename="datasets40_satellite_product"

    elif selection=="41":
        regex=".*_topography_.*"
        filename="datasets41_topography"

    elif selection=="42":
        regex=".*_LOCA_.*"
        filename="datasets42_LOCA"

    elif selection=="43":
        regex=".*_SCSPOD14_.*"
        filename="datasets43_SCSPOD14"
	
    elif selection=="44":
        regex=".*_OfES_.*"
        filename="datasets0_ofes"

    elif selection=="45":
        regex=".*_HYCOM_.*"
        filename="datasets0_hycom"

    elif selection=="46":
        regex=".*Modeling_marine_debris_drift_from_2011_tsunami.*"
        filename="datasets44_2011_Tsunami_debris_drift" 
 
    subprocess.call([command + " " + option1 + " " + option2 + "  " + regex + " " + option3], shell=True)
    print "#########################" 
    print "# done with generation! #"
    print "#########################"
    #clean up the created file
    subprocess.call(["sed","-i", "s/HAWAII SOEST/APDRC/g","./temp/EDDGridFromThreddsCatalog.xml"])
    subprocess.call(["sed","-i", "s/data apdrc.soest.hawaii.edu dods public data //g","./temp/EDDGridFromThreddsCatalog.xml"])
    subprocess.call(["sed","-i", "s/data apdrc.soest.hawaii.edu 80 dods public data //g","./temp/EDDGridFromThreddsCatalog.xml"]) 
    #subprocess.call(["sed -n \'/SUMMARY/q;p\' ./temp/EDDGridFromThreddsCatalog.xml | tee ./temp/EDDGridFromThreddsCatalog3.xml"],shell=True) 
    #time.sleep(1)
    return filename

def genPrivate():
    """
    There are no private ERDDAP datasets, but this function performs the same task as genPublic. 
    It's not complete.
    """




    selection = raw_input("Select from the above: ")
    #print selection
    if int(selection) > 10 or int(selection) < 1:
        print("invalid input")
        exit()
    os.chdir("/usr/local/tomcat2/webapps/erddap/WEB-INF")

    command = "/usr/local/tomcat2/webapps/erddap/WEB-INF/GenerateDatasetsXml.sh"
    option1 = "EDDGridFromThreddsCatalog"
    option2 = "http://apdrc5.soest.hawaii.edu:9191/thredds/catalog/las_iprc/catalog.xml"
    option3 = "\"\""

    if selection=="1":
        regex = ".*AfES_.*"
        filename = "datasets1i_AfES"
    elif selection=="2":
        regex = ".*_CRU_.*"
        filename = "datasets2i_CRU"
    elif selection=="3":
        regex = ".*_ECMWF_.*"
        filename = "datasets3i_ECMWF"
    elif selection=="4":
        regex = ".*_India_Rainfall_.*"
        filename = "datasets4i_India_Rainfall"
    elif selection=="5":
        regex = ".*_JRA-25_.*"
        filename = "datasets5i_JRA-25"
    elif selection=="6":
        regex = ".*_MRI-JMA_.*"





def printPublicDatasets():
    """
    Prints a list of every dataset category in ERDDAP.
    Parameters: None
    Returns: Nothing
    """

    print("1: Argo Products\t\t2: CFSv2")
    print("3: CMIP5\t\t\t4: CSIRO Atlas")
    print("5: CliPAS\t\t\t6: CDASK1.4")
    print("7: ECCO2\t\t\t8: ERA-40")
    print("9: ERA75deg\t\t\t10:FRA-JCOPE2")
    print("11:GAME\t\t\t\t12:GFDL")
    print("13:HadSST\t\t\t14:ISVHE")
    print("15:Interpolated Precipitation\t16:J-OFURO")
    print("17:KYUSHU\t\t\t18:Model output")
    print("19:NCOM\t\t\t\t20:NLOM")
    print("21:NLOM32\t\t\t22:NOAA SST")
    print("23:Ocean climatology\t\t24:PODAAC")
    print("25:PRIDE\t\t\t26:Paleoclimate modeling")
    print("27:Reanalysis Data\t\t28:SCUD")
    print("29:SOCAT\t\t\t30:SODA")
    print("31:Tohoku\t\t\t32:Typhoon Reanalysis")
    print("33:WASWind\t\t\t34:WHOI OAFlux")
    print("35:WOA\t\t\t\t36:bimodal ISO index")
    print("37:hydrobase\t\t\t38:hydrological data")
    print("39:iCOADS\t\t\t40:Satellite Product")
    print("41:topography\t\t\t42:Loca")
    print "43:SCSPOD14\t\t\t44:ofes\t\t\t"
    print "45:ofes HYCOM"
    print "46:2011 Tsunami Debris Drift Modeling"

def printPrivateDatasets():
    """ 
    Prints the private datasets. Not currently in use.
    """

    print ("1: AfES \t\t\t 2: CRU")
    print ("3: ECMWF \t\t\t 4: India Rainfall")
    print ("5: JRA-25 \t\t\t 6: MRI-JMA")
    print "7: Model Output \t\t 8: gebco 1min bathy"
    print "9: IROAM \t\t\t 10: Satellite Product"



if __name__ == "__main__":
    main()


