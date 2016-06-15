import pandas as pd
import collections
import operator
import sys
import timeit
import glob
import datetime

#PATH = '/users/bhishma/Documents/JubaPlus/Celebrity'


class Node(object):

    def __init__(self, d, t, i):
        self.date = d
        self.time = t
        self.id = i

def sessionTime(start, end): #Assumption on var is the session duration is never more than 24 hours

    sec = end - start
    hh = format(sec/3600, '02') if sec/3600 else format(0, '02')
    sec = sec - int(hh) * 3600
    mm = format(sec/60, '02') if sec/60 else format(0, '02')
    sec = sec - int(mm) * 60
    ss= format(sec, '02')

    x = [str(hh), str(mm), str(ss)]

    return ':'.join(x)

def main():

    #global PATH

    time_start = timeit.default_timer() 

    df = pd.read_csv('/home/dummy/try/fileNewFinalUS.tsv', header=None, delimiter="\t", error_bad_lines = False)

    #df = pd.read_csv(PATH + '/data/testFileFile1.tsv', header=None, delimiter="\t", error_bad_lines = False)

    print 'file read'
    #print len(df1.index)
    df.columns = ['U','SC','C','URL','D','T']

    #df = df1.loc[df1['C'] == 'US']
    print len(df.index)
    #df.to_csv('/home/dummy/try/fileNewFinalUS' + '.tsv', index = False, header= None, sep='\t')
    #print 'donewa'
    #df.columns = ['U','SC','C','URL','D','T']
    session = []
    session.append(1)
    dur = ['00:00:00' for i in range(len(df.index))]
   
    

    seconds = df['T'].str.strip(' GMT').str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))

    
    print seconds.head(3)


    for row in df.itertuples():
        prev_row = row
        break

    

    ses_row = prev_row
    
    for row in df.itertuples():
        try:
            g = 1/int(row[0])
            
            if(prev_row[1] == row[1]): #same user
                if prev_row[5] == row[5]:
                    if seconds.at[row[0]] - seconds.at[prev_row[0]] < 3600:
                        session.append(session[prev_row[0]])
                    else:
                        session.append(session[prev_row[0]]+1)
                        if ses_row[5] == prev_row[5]:
                            duration = sessionTime(seconds.at[ses_row[0]], seconds.at[prev_row[0]])
                        else:
                            a = map(int, prev_row[5].split('-'))
                            b = map(int, ses_row[5].split('-'))

                            d1 = datetime.datetime(a[0],a[1],a[2])
                            d2 = datetime.datetime(b[0],b[1],b[2])
                            d = (d1 - d2).days
                            s_var = seconds.at[prev_row[0]] + (d*86400)
                            duration = sessionTime(seconds.at[ses_row[0]], s_var)

                        for i in range(ses_row[0],row[0]):
                            dur[i] = duration

                        ses_row = row
                else:
                    p = map(int, row[5].split('-'))
                    q = map(int, prev_row[5].split('-'))                

                    xx = datetime.datetime(p[0],p[1],p[2])
                    yy = datetime.datetime(q[0],q[1],q[2])
                    d = (xx - yy).days

                    if d == 1:
                        tt = seconds.at[row[0]] - seconds.at[prev_row[0]] + 86400
                    else:
                        tt = 3600

                    if tt < 3600:
                        session.append(session[prev_row[0]])
                    else:
                        r = map(int, ses_row[5].split('-'))
                        zz = datetime.datetime(r[0],r[1],r[2])

                        dn = (yy - zz).days

                        secs = seconds.at[prev_row[0]] - seconds.at[ses_row[0]] + (dn*86400)

                        session.append(session[prev_row[0]]+1)
                        duration = sessionTime(0, secs)

                        for i in range(ses_row[0],row[0]):
                            dur[i] = duration

                        ses_row = row

            else:
                session.append(1)
                if ses_row[5] == prev_row[5]:
                    duration = sessionTime(seconds.at[ses_row[0]], seconds.at[prev_row[0]])
                else:
                    p = map(int, prev_row[5].split('-'))
                    q = map(int, ses_row[5].split('-'))                

                    xx = datetime.datetime(p[0],p[1],p[2])
                    yy = datetime.datetime(q[0],q[1],q[2])
                    d = (xx - yy).days

                    s_var = seconds.at[prev_row[0]] + (d*86400)
                    duration = sessionTime(seconds.at[ses_row[0]], s_var)

                for i in range(ses_row[0],row[0]):
                    dur[i] = duration
                    
                ses_row = row

            prev_row = row

        except ZeroDivisionError as e:
            print 'exception raised'
            pass

    t1 = seconds.iat[len(seconds.index)-1] 
    t2 = seconds.at[ses_row[0]]
    duration = sessionTime(t2, t1)
    for i in range(ses_row[0], len(seconds.index)):
        dur[i] = duration



    print len(df.index), len(session), len(dur)

    df.insert(1, 'a', session)
    df.insert(2, 'b', dur)

    print len(df.index)
        
    #df.to_csv("/home/dummy/try/SesOutFinal.tsv", index = False, header= False, sep='\t')
    df.to_csv('/home/dummy/try/SesOutFinalUS' + '.tsv', index = False, header= None, sep='\t')


    time_stop = timeit.default_timer()

    print time_stop - time_start

    


if __name__=="__main__": main()


