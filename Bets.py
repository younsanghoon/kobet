def Bet(o1,Rads,Blacks,Nber1s,Nber2s,ups,douns):
    nm = int(data['args']['numbers']['results'][0][0]['number'])
    print ('이머징 룰렛',nm)
    if nmaa1 == 0:
        for i in range(len(data['args']['numbers']['results'])):
            nm1.append(int(data['args']['numbers']['results'][i][0]['number']))
            nmaa1 +=1
        if nmaa1 == 12:
            #print(nm1)
            nm1.reverse()
            #print(nm1)
            for Cmn in range(len(nm1)):
                Cmns = int(nm1[Cmn])
                print(nm1[Cmn])
                o1 +=1
                if o1 < 12:
                    print (o1,'o1')
                    if Cmns == 0:
                        Rads +=1
                        Blacks +=1
                        Nber1s +=1
                        Nber2s +=1
                        ups +=1
                        douns +=1
                        print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                    else:
                        if Cmns%2==1:
                            Nber1s +=1
                            Nber2s =0
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        else:
                            Nber1s =0
                            Nber2s +=1
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        if Rad.count(Cmns):
                            Rads +=1
                            Blacks = 0
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        else:
                            Blacks +=1
                            Rads = 0
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        if Cmns >= 1 and Cmns <= 18:
                            douns +=1
                            ups =0
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
                        else:
                            ups +=1
                            douns = 0
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
    elif nm == 0:
        Rads +=1
        Blacks +=1
        Nber1s +=1
        Nber2s +=1
        ups +=1
        douns +=1
        print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
    else:
        if nm%2==1:
            Nber1s +=1
            Nber2s =0
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
            Nber1s =0
            Nber2s +=1
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        if Rad.count(nm):
            Rads +=1
            Blacks = 0
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
            Blacks +=1
            Rads = 0
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        if nm >= 1 and nm <= 18:
            douns +=1
            ups =0
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
            ups +=1
            douns = 0
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        if Nber1s == 4 :
            print ('짝수 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        elif Nber1s > 4 :
            print ('짝수 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        if Rads == 4:
            print('블랙 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        elif Rads > 4:
            print('블랙 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
           print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        if ups == 4:
            print('다운 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        elif ups > 4:
            print('다운 2배 배팅','홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
        else:
                            print('홀수:',Nber1s, '짝수:',Nber2s, '레드:',Rads, '블랙:', Blacks, '업:',ups, '다운:',douns)
