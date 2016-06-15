import rha
import adv


if __name__ == "__main__":
        #fout = open('HHIDPersonIBFVCITDNonBlankPaidAnalysis.csv','w');
        #fout = open('HHIDPersonILAHNonBlankPaidAnalysis.csv','w');
        fout = open('/disk2/PostAnalysis/guhhpostanal/nonblank/HHIDPersonIGUHHNonBlankPaidAnalysis-test-5.csv','w');
        fout1 = open('gwt25541.csv','w');
        header = 'Network\tProgram(From Logfile)\tProgram(From 30)\tTelecastID\tDate\tBroadcast Start Time\tBroadcast End Time\tPostLogTime\tLength\tSource\tMarket\tType\tCost\t'
        header1 = 'HHID\tPersonID\tNetwork\tProgram\tTelecast\tAge\tSexCode\tViewership Date\tStart Time\tEnd Time\tTimeShiftedViewingCode\t'
	header1+='MinimumPlayDelay\tVCRRecordOnlyIndicator\tHeadOfHouseHoldRace\tGeographicTerritoryCode\tTZC\tCSC\tLMPFlag\tLMPMarketCode\tMVPD\tPersonMonthlyUnifiedWt\tHouseHoldMonthlyUnifiedW\tHH In-Tab Wt\tPerson In-Tab Wt\tExposeToAdv\n';
        fout.write(header+header1);
        fout1.write(header+header1);
        path = '/home/account1/marymary/';
	#showlistdict,advdatesetdict = adv.readaddfiles('nonblank.csv-b')
	#showlistdict,advdatesetdict = adv.readaddfiles('nonblank.csv')
	#showlistdict,advdatesetdict = adv.readaddfiles('lahnonblankpaid.csv')
	showlistdict,advdatesetdict = adv.readaddfiles('guhhnonblankpaid.csv')
        rha.showoutput(path,fout,fout1,showlistdict,advdatesetdict)
        fout.close();
	print 'arnab'
