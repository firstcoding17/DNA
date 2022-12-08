# This is a sample Python script.
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import json
import requests
# Press ShiftF10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def Main():

    df1_x = pd.read_excel(r'C:\DNA\CCTVData.xlsx')#CCTV정보들 (주소,  설치연월) 컬럼 이용

    df1_y = pd.read_csv(r'C:\DNA\CrimeData1.csv')#대검찰청청범죄발생지 2018년도
    df2_y = pd.read_csv(r'C:\DNA\CrimeData2.csv')#대검찰청청범죄발생지 2019년도

    #clustering_byinsert = list(df1_x['설치연월'].unique()) 행 종류 확인용




    df1_s2019 = df1_x[(df1_x['설치연월'] != '2020-01') & (df1_x['설치연월'] != '2020-02') & (df1_x['설치연월'] != '2020-03') & (df1_x['설치연월'] != '2020-04') &
                      (df1_x['설치연월'] != '2020-05') & (df1_x['설치연월'] != '2020-06') & (df1_x['설치연월'] != '2020-07') & (df1_x['설치연월'] != '2020-08') & (df1_x['설치연월'] != '2020-09')
                      &
                       (df1_x['설치연월'] != '2020-10') & (df1_x['설치연월'] != '2020-11') & (df1_x['설치연월'] != '2020-12') &
                      (df1_x['설치연월'] != '2021-01') & (df1_x['설치연월'] != '2021-02') & (df1_x['설치연월'] != '2021-03') &
                       (df1_x['설치연월'] != '2021-04') &
                        (df1_x['설치연월'] != '2021-05') & (df1_x['설치연월'] != '2021-06') & (df1_x['설치연월'] != '2021-07') &
                         (df1_x['설치연월'] != '2021-08') & (df1_x['설치연월'] != '2021-09') &
                          (df1_x['설치연월'] != '2021-10') & (df1_x['설치연월'] != '2021-11') & (df1_x['설치연월'] != '2021-12') &
                           (df1_x['설치연월'] != '2022-01') & (df1_x['설치연월'] != '2022-02') & (df1_x['설치연월'] != '2022-03') &
                            (df1_x['설치연월'] != '2022-04') &
                             (df1_x['설치연월'] != '2022-05') & (df1_x['설치연월'] != '2022-06') & (df1_x['설치연월'] != '2022-07') &
                              (df1_x['설치연월'] != '2022-08') & (df1_x['설치연월'] != '2022-09') &
                               (df1_x['설치연월'] != '2022-10') & (df1_x['설치연월'] != '2022-11') & (df1_x['설치연월'] != '2021-12') &
                                (df1_x['설치연월'] != '2020-.7')
                      ]
    #print(df1_s2019['설치연월'].unique()) 20년 이후 설치된 CCTV삭제

    df1_s2018 = df1_x[(df1_x['설치연월'] != '2020-01') & (df1_x['설치연월'] != '2020-02') & (df1_x['설치연월'] != '2020-03') & (df1_x['설치연월'] != '2020-04') &
                      (df1_x['설치연월'] != '2020-05') & (df1_x['설치연월'] != '2020-06') & (df1_x['설치연월'] != '2020-07') & (df1_x['설치연월'] != '2020-08') & (df1_x['설치연월'] != '2020-09')
                      &
                       (df1_x['설치연월'] != '2020-10') & (df1_x['설치연월'] != '2020-11') & (df1_x['설치연월'] != '2020-12') &
                      (df1_x['설치연월'] != '2021-01') & (df1_x['설치연월'] != '2021-02') & (df1_x['설치연월'] != '2021-03') &
                       (df1_x['설치연월'] != '2021-04') &
                        (df1_x['설치연월'] != '2021-05') & (df1_x['설치연월'] != '2021-06') & (df1_x['설치연월'] != '2021-07') &
                         (df1_x['설치연월'] != '2021-08') & (df1_x['설치연월'] != '2021-09') &
                          (df1_x['설치연월'] != '2021-10') & (df1_x['설치연월'] != '2021-11') & (df1_x['설치연월'] != '2021-12') &
                           (df1_x['설치연월'] != '2022-01') & (df1_x['설치연월'] != '2022-02') & (df1_x['설치연월'] != '2022-03') &
                            (df1_x['설치연월'] != '2022-04') &
                             (df1_x['설치연월'] != '2022-05') & (df1_x['설치연월'] != '2022-06') & (df1_x['설치연월'] != '2022-07') &
                              (df1_x['설치연월'] != '2022-08') & (df1_x['설치연월'] != '2022-09') &
                               (df1_x['설치연월'] != '2022-10') & (df1_x['설치연월'] != '2022-11') & (df1_x['설치연월'] != '2021-12') &
                                (df1_x['설치연월'] != '2020-.7') &
                      (df1_x['설치연월'] != '2019-01') & (df1_x['설치연월'] != '2019-02') & (df1_x['설치연월'] != '2019-03') &
                      (df1_x['설치연월'] != '2019-04') &
                      (df1_x['설치연월'] != '2019-05') & (df1_x['설치연월'] != '2019-06') & (df1_x['설치연월'] != '2019-07') &
                      (df1_x['설치연월'] != '2019-08') & (df1_x['설치연월'] != '2019-09') &
                      (df1_x['설치연월'] != '2019-10') & (df1_x['설치연월'] != '2019-11') & (df1_x['설치연월'] != '2019-12')
                      ]
    #print(df1_s2018['설치연월'].unique()) 19년 이후 "

    #2018년 서울특별시 한정 범죄 일어난 총 건 330403
    '''
    print(df1_y['서울_종로'].sum()+df1_y['서울_중구'].sum()+df1_y['서울_용산'].sum()+df1_y['서울_성동'].sum()+
      df1_y['서울_광진'].sum()+df1_y['서울_동대문'].sum()+df1_y['서울_중랑'].sum()+df1_y['서울_성북'].sum()+
      df1_y['서울_강북'].sum()+df1_y['서울_노원'].sum()+df1_y['서울_노원'].sum()+
      df1_y['서울_은평'].sum()+df1_y['서울_서대문'].sum()+df1_y['서울_마포'].sum()+df1_y['서울_양천'].sum()+
      df1_y['서울_구로'].sum()+df1_y['서울_금천'].sum()+df1_y['서울_영등포'].sum()+df1_y['서울_동작'].sum()+
      df1_y['서울_관악'].sum()+df1_y['서울_서초'].sum()+df1_y['서울_강남'].sum()+df1_y['서울_송파'].sum()+
      df1_y['서울_강동'].sum())
    '''


    #2019년 서울특별시 한정 범죄 일어난 총 건 328658
    '''
    print(df2_y['서울_종로'].sum()+df2_y['서울_중구'].sum()+df2_y['서울_용산'].sum()+df2_y['서울_성동'].sum()+
      df2_y['서울_광진'].sum()+df2_y['서울_동대문'].sum()+df2_y['서울_중랑'].sum()+df2_y['서울_성북'].sum()+
      df2_y['서울_강북'].sum()+df2_y['서울_노원'].sum()+df2_y['서울_노원'].sum()+
      df2_y['서울_은평'].sum()+df2_y['서울_서대문'].sum()+df2_y['서울_마포'].sum()+df2_y['서울_양천'].sum()+
      df2_y['서울_구로'].sum()+df2_y['서울_금천'].sum()+df2_y['서울_영등포'].sum()+df2_y['서울_동작'].sum()+
      df2_y['서울_관악'].sum()+df2_y['서울_서초'].sum()+df2_y['서울_강남'].sum()+df2_y['서울_송파'].sum()+
      df2_y['서울_강동'].sum())
    '''


    #CCTV 서울만 데이터 가져오기



    #2018년한정 서울특별시 CCTV대비 범죄 발생 분석




    #1 상관관계분석 2018년까지 데이터만
    #index_y 구한 코드 모든 범죄
    '''
    region = ['서울_종로','서울_중구','서울_용산','서울_성동','서울_광진','서울_동대문','서울_중랑','서울_성북',
          '서울_강북','서울_도봉','서울_노원','서울_은평','서울_서대문','서울_마포','서울_양천','서울_강서','서울_구로',
          '서울_금천','서울_영등포','서울_동작','서울_관악','서울_서초','서울_강남','서울_송파','서울_강동']
    listup=list()
    for i in range(0,len(region)):
        listup.append(df1_y[region[i]].sum())
        

    '''

    # 2018 (5대 범죄 + @)만
    '''
    list_a = ['서울_종로', '서울_종로', '서울_용산','서울_성동','서울_광진', '서울_동대문', '서울_중랑', '서울_성북', '서울_강북', '서울_노원', '서울_은평','서울_서대문',
              '서울_마포', '서울_양천', '서울_구로', '서울_금천', '서울_영등포', '서울_동작', '서울_관악','서울_서초','서울_강남', '서울_송파','서울_강동']
    list_b = [0, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 31, 35, 37, 38, 39, 40, 43, 46, 67, 81, 82, 83, 84, 85, 86, 150, 140, 148, 152, 157, 143]


    total_list =list()
    for i in range(0,len(list_a)):
        a = 0
        for j in range(0,len(list_b)):
            a+=df2_y[list_a[i]][list_b[j]].sum()
        total_list.append(a)
    print(total_list)
    '''

    Index_y = [11700, 12720, 10820, 8785, 11289, 11363, 11353, 9465, 9821, 11615, 10345, 8973, 15886, 10713, 16009, 13874, 10448, 19142, 9273, 16088, 21999, 34757, 20116, 11003]#모든 범죄
    Index_y_1 =[5465, 5465, 5694, 4222, 5902, 5885, 6066, 5037, 5127, 3223, 5978, 5374, 4142, 8103, 5506, 6746, 4566, 9397, 4902, 8081, 8601, 13622, 9870, 5592]#5대범죄 + @만 152566개개
    '''
   region = ['서울특별시 종로', '서울특별시 중구', '용산', '서울특별시 성동', '서울특별시 광진', '서울특별시 동대문', '서울특별시 중랑', '서울특별시 성북',
          '서울특별시 강북', '도봉', '서울특별시 노원', '서울특별시 은평', '서울특별시 서대문', '서울특별시 마포', '양천', '서울특별시 강서', '서울특별시 구로',
          '서울특별시 금천', '서울특별시 영등포', '동작', '서울특별시 관악', '서초', '서울특별시 강남', '서울특별시 송파', '서울특별시 강동'] 
    listup = list()
    for i in range(0, len(region)):
        listup.append(df1_s2018[df1_s2018['관리기관명'].str.contains(region[i])]['카메라대수'].sum())
    print(listup)

    print(df1_s2018['관리기관명'].unique())
    '''
    Index_x = [1534, 2460, 2039, 2612, 2846, 2502, 4460, 3104, 1267, 1710, 4775, 2940, 1933, 5653, 2867, 3449, 2393, 4307, 6616, 4785, 6222, 6397, 1452, 1577]




    total_list = [Index_y,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)
    #상관관계 그래프
    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('All crimes and the number of CCTVs in each Seoul district office in 2018')
    plt.show()

    #회귀모델
    results = sm.OLS(Index_y, sm.add_constant(Index_x)).fit()
    print(results.summary())

    plt.scatter(Index_x, Index_y)
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2018')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]*1.3855+9035.7308)
    plt.scatter(Index_x,Index_y)
    plt.plot(Index_x,ploty,c='black')
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('All crimes and the number of CCTVs in each Seoul district office in 2018 with regression')
    plt.show()

    total_list = [Index_y_1,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)
    #상관관계 그래프
    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018')
    plt.show()


    #결과 양의 상관관계가 있음 0.417972
    results = sm.OLS(Index_y_1, sm.add_constant(Index_x)).fit()
    print(results.summary())

    plt.scatter(Index_x,Index_y_1)
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]* 0.7206+3958.0712)
    plt.scatter(Index_x,Index_y_1)
    plt.plot(Index_x,ploty,c='black')
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018 with regression')
    plt.show()


    #" 2019년이후 모든 범죄 데이터 전처리
    '''
    region = ['서울_종로', '서울_중구', '서울_용산', '서울_성동', '서울_광진', '서울_동대문', '서울_중랑', '서울_성북',
          '서울_강북', '서울_노원', '서울_은평', '서울_서대문', '서울_마포', '서울_양천', '서울_강서', '서울_구로',
          '서울_금천', '서울_영등포', '서울_동작', '서울_관악', '서울_서초', '서울_강남', '서울_송파', '서울_강동']
    listup = list()
    for i in range(0, len(region)):
        listup.append(df2_y[region[i]].sum())
    print(listup)
    '''

    # 2019이후 (5대 범죄 + @)만 데이터 전처리
    '''
    list_a = ['서울_종로', '서울_종로', '서울_용산','서울_성동','서울_광진', '서울_동대문', '서울_중랑', '서울_성북', '서울_강북', '서울_노원', '서울_은평','서울_서대문',
              '서울_마포', '서울_양천', '서울_구로', '서울_금천', '서울_영등포', '서울_동작', '서울_관악','서울_서초','서울_강남', '서울_송파','서울_강동']
    list_b = [0, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 31, 35, 37, 38, 39, 40, 43, 46, 67, 81, 82, 83, 84, 85, 86, 150, 140, 148, 152, 157, 143]


    total_list =list()
    for i in range(0,len(list_a)):
        a = 0
        for j in range(0,len(list_b)):
            a+=df2_y[list_a[i]][list_b[j]].sum()
        total_list.append(a)
    print(total_list)
    '''

    Index_y = [12132, 13706, 10500, 8846, 11225, 11510, 11491, 9444, 10482, 11463, 10631, 8714, 14814, 10104, 16001, 13421, 10309, 17945, 9625, 15971, 22780, 33898, 20302, 11067]#모든 범죄
    Index_y_1 =[5504, 5504, 5244, 4095, 5776, 5657, 6042, 5131, 5346, 3083, 6007, 5225, 4291, 7411, 5118, 6561, 4403, 8860, 5131, 7881, 9033, 13391, 9573, 5717]#5대범죄 + @만 149984개
    '''
    2019년 CCTV개수 구하는 데이터 전처리식
    region = ['서울특별시 종로', '서울특별시 중구', '용산', '서울특별시 성동', '서울특별시 광진', '서울특별시 동대문', '서울특별시 중랑', '서울특별시 성북',
          '서울특별시 강북', '서울특별시 노원', '서울특별시 은평', '서울특별시 서대문', '서울특별시 마포', '양천', '서울특별시 강서', '서울특별시 구로',
          '서울특별시 금천', '서울특별시 영등포', '동작', '서울특별시 관악', '서초', '서울특별시 강남', '서울특별시 송파', '서울특별시 강동']

    listup = list()
    for i in range(0, len(region)):
        listup.append(df1_s2019[df1_s2019['관리기관명'].str.contains(region[i])]['카메라대수'].sum())
    print(listup)
    '''
    Index_x = [1559, 2460, 2039, 3103, 2846, 2502, 4460, 3560, 1774, 1972, 6369, 2940, 2316, 5901, 2867, 3723, 2393, 4307, 6616, 4785, 6939, 6397, 2537, 1933]
    total_list = [Index_y,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)
    # 상관관계 그래프
    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2019')
    plt.show()

    results = sm.OLS(Index_y, sm.add_constant(Index_x)).fit()
    print(results.summary())


    plt.scatter(Index_x,Index_y)
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('All crimes and the number of CCTVs in each Seoul district office in 2019')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]*1.2975+8933.5499)
    plt.scatter(Index_x,Index_y)
    plt.plot(Index_x,ploty,c='black')
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('All crimes and the number of CCTVs in each Seoul district office in 2019 with regression')
    plt.show()






    total_list = [Index_y_1,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)
    # 상관관계 그래프
    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019')
    plt.show()

    results = sm.OLS(Index_y_1, sm.add_constant(Index_x)).fit()
    print(results.summary())

    plt.scatter(Index_x,Index_y_1)
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]* 0.7103 + 3695.1491)
    plt.scatter(Index_x,Index_y_1)
    plt.plot(Index_x,ploty,c='black')
    plt.xlabel('CCTV')
    plt.ylabel('Crime')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019 with regression')
    plt.show()

    #각 지역구마다 총생활인구수와 CCTV개수에 따른 범죄율의 변화

    '''
    총생활인구수 전처리
    datelist_y = [20180500, 20180600, 20180700, 20180800, 20180900, 20181000, 20181100, 20181200, 20190100, 20190200, 20190300, 20190400,
              20190500, 20190600, 20190700, 20190800, 20190900, 20191000, 20191100, 20191200, 20200100, 20200200, 20200300, 20200400]
    total_region = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구',
          '강북구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구',
          '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']

    datelist_x = [20190500, 20190600, 20190700, 20190800, 20190900, 20191000, 20191100, 20191200, 20200100, 20200200, 20200300, 20200400,
              20200500, 20200600, 20200700, 20200800, 20200900, 20201000, 20201100, 20201200, 20210100, 20210200, 20210300, 20210400]

    #인구수 손실된 2018년도 1월 ~ 4월 데이터 회귀식으로 구하기 print(pop.corr()['총생활인구수'])


    #지역 상관 x 월기준 평균 총생활인구수 이 회귀식으로 잃어버린 2018년도 1월 ~ 4월 데이터 생성 후 각 지역 연평균 총생활인구수로 데이터 셋 구성



    train_x = list()
    test_y = list()
    for i in range(0,len(datelist_x)):
        train_x.append(pop[(pop['기준일ID'] > datelist_x[i]) & (pop['기준일ID'] < datelist_x[i] + 32)][["총생활인구수","주간인구수(09~18)","서울외유입인구수"]].sum())
        test_y.append(pop[(pop['기준일ID'] > datelist_y[i]) & (pop['기준일ID'] < datelist_y[i] + 32)]['총생활인구수'].sum())


    results = sm.OLS(test_y,sm.add_constant(train_x)).fit()
    print(results.summary())



    coef = [-28.0589, 28.2793, -6.4014,7.236*(10**8)]#상수는 7.236e+08

    to_insert_infor = [ 20190100, 20190200, 20190300, 20190400]

    region_2018 = list()

    datelist = [20180500, 20180600, 20180700, 20180800, 20180900, 20181000, 20181100, 20181200]
    for i in range(0,len(total_region)):
        num = 0
        x = pop[pop['시군구명'] == total_region[i]]

        for j in range(0, len(to_insert_infor)):
            x1 = x[(x['기준일ID'] > to_insert_infor[j]) & (x['기준일ID'] < to_insert_infor[j] + 32)]["총생활인구수"].sum()
            x2 = x[(x['기준일ID'] > to_insert_infor[j]) & (x['기준일ID'] < to_insert_infor[j] + 32)]["주간인구수(09~18)"].sum()
            x3 = x[(x['기준일ID'] > to_insert_infor[j]) & (x['기준일ID'] < to_insert_infor[j] + 32)]["서울외유입인구수"].sum()
            num += (x1 * coef[0] + x2 * coef[1] + x3 * coef[2] + coef[3])
        for j in range(0,len(datelist)):
            num+= x[(x['기준일ID'] > datelist[j]) & (x['기준일ID'] < datelist[j] + 32)]["총생활인구수"].sum()
        num = num/12
        region_2018.append(num)
    print(region_2018)
    print(len(region_2018))

    region_2019 =list()
    datelist = [20190100, 20190200, 20190300, 20190400,20190500, 20190600, 20190700, 20190800, 20190900, 20191000, 20191100, 20191200]
    for i in range(0,len(total_region)):
        num = 0
        x = pop[pop['시군구명'] == total_region[i]]
        for j in range(0,len(datelist)):
            num += x[(x['기준일ID'] > datelist[j]) & (x['기준일ID'] < datelist[j] + 32)]["총생활인구수"].sum()
        num = num / 12
        region_2019.append(num)
    print(region_2019)
    print(len(region_2019))

    #2018 [268332695.18025208, 274315314.555293, 252505709.40360352, 249142168.8544104, 243623213.52557495, 248049207.91711554, 239505606.90743306, 243414105.05873683, 240435026.69427046, 242274308.76490095, 237971594.87015226, 249983410.06114307, 254206164.20195913, 241479527.55071864, 243032616.811089, 245263691.2117305, 247560581.556427, 261654289.9321353, 241533364.36802444, 237335886.35138956, 271274593.72738653, 291140140.7969622, 253137359.59418714, 241433989.6718892]
    #2019 [9954948.548266666, 10713541.171091665, 9552646.090625001, 10676442.656083332, 11888226.918441666, 11497522.11255, 10610898.583291667, 13115688.540699998, 8917762.894824998, 15419017.791466668, 13053803.795683334, 12071287.250908336, 14993229.734458333, 11693030.71825833, 16309504.15675, 12476688.465091666, 7010471.810216666, 15094435.003725, 12351614.010299997, 15020973.397799999, 18073669.907725, 24988427.80548333, 22935894.541983336, 14303044.943258332]

    
    '''

    Index_y = [11700, 12720, 10820, 8785, 11289, 11363, 11353, 9465, 9821, 11615, 10345, 8973, 15886, 10713, 16009,
               13874, 10448, 19142, 9273, 16088, 21999, 34757, 20116, 11003]  # 모든 범죄

    Index_y_1 = [5465, 5465, 5694, 4222, 5902, 5885, 6066, 5037, 5127, 3223, 5978, 5374, 4142, 8103, 5506, 6746, 4566,
                 9397, 4902, 8081, 8601, 13622, 9870, 5592]  # 5대범죄 + @만 152566개개

    pop2018 =  [268332695.18025208, 274315314.555293, 252505709.40360352, 249142168.8544104, 243623213.52557495, 248049207.91711554,
                239505606.90743306, 243414105.05873683, 240435026.69427046, 242274308.76490095, 237971594.87015226, 249983410.06114307,
                254206164.20195913, 241479527.55071864, 243032616.811089, 245263691.2117305, 247560581.556427, 261654289.9321353,
                241533364.36802444, 237335886.35138956, 271274593.72738653, 291140140.7969622, 253137359.59418714, 241433989.6718892] #2018년 각 지역구 총생활인구

    Index_x = [1534, 2460, 2039, 2612, 2846, 2502, 4460, 3104, 1267, 1710, 4775, 2940, 1933, 5653, 2867, 3449, 2393,
               4307, 6616, 4785, 6222, 6397, 1452, 1577]

    total_list = [Index_y,pop2018,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)

    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()

    df_x = pd.DataFrame({
        'x1' : Index_x,
        'x2' : pop2018
    })

    results = sm.OLS(Index_y, sm.add_constant(df_x)).fit()
    print(results.summary())





    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2018,Index_y)

    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]*0.9677+pop2018[i]*0.0003-6.133*(10**4))

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2018,Index_y)
    ax.scatter(Index_x, pop2018,ploty,c='black')

    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()



    total_list = [Index_y_1,pop2018,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)
    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()
    # 결과 양의 상관관계가 있음 0.5 0.5
    df_x = pd.DataFrame({
        'x1': Index_x,
        'x2': pop2018
    })

    results = sm.OLS(Index_y_1, sm.add_constant(df_x)).fit()
    print(results.summary())

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2018,Index_y_1)

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()

    ploty = list()
    for i in range(0,len(Index_x)):
        ploty.append(Index_x[i]*0.6031+pop2018[i]*(8.046/100000)-1.583*(10**4))

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2018,Index_y_1)
    ax.scatter(Index_x, pop2018,ploty,c='black')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2018 with pop_infore')
    plt.show()







    Index_y = [12132, 13706, 10500, 8846, 11225, 11510, 11491, 9444, 10482, 11463, 10631, 8714, 14814, 10104, 16001,
               13421, 10309, 17945, 9625, 15971, 22780, 33898, 20302, 11067]  # 모든 범죄

    Index_y_1 = [5504, 5504, 5244, 4095, 5776, 5657, 6042, 5131, 5346, 3083, 6007, 5225, 4291, 7411, 5118, 6561, 4403,
                 8860, 5131, 7881, 9033, 13391, 9573, 5717]  # 5대범죄 + @만 149984개

    pop2019 = [9954948.548266666, 10713541.171091665, 9552646.090625001, 10676442.656083332, 11888226.918441666, 11497522.11255,
               10610898.583291667, 13115688.540699998, 8917762.894824998, 15419017.791466668, 13053803.795683334, 12071287.250908336,
               14993229.734458333, 11693030.71825833, 16309504.15675, 12476688.465091666, 7010471.810216666, 15094435.003725,
               12351614.010299997, 15020973.397799999, 18073669.907725, 24988427.80548333, 22935894.541983336, 14303044.943258332]#2019년 각 지역구 총생활인구

    Index_x = [1559, 2460, 2039, 3103, 2846, 2502, 4460, 3560, 1774, 1972, 6369, 2940, 2316, 5901, 2867, 3723, 2393,
               4307, 6616, 4785, 6939, 6397, 2537, 1933]


    total_list = [Index_y,pop2019,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)

    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()

    df_x = pd.DataFrame({
        'x1': Index_x,
        'x2': pop2019
    })

    results = sm.OLS(Index_y, sm.add_constant(df_x)).fit()
    print(results.summary())

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2019, Index_y)

    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()

    ploty = list()
    for i in range(0, len(Index_x)):
        ploty.append(Index_x[i] *  0.3319 + pop2019[i] * 0.0011  -2483.2399)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2019, Index_y)
    ax.scatter(Index_x, pop2019, ploty, c='black')

    plt.title('all crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()








    total_list = [Index_y_1,pop2019,Index_x]
    total_df = pd.DataFrame(total_list).T
    corr = total_df.corr(method='pearson')
    print(corr)

    cmap = sns.light_palette("darkgray", as_cmap=True)
    sns.heatmap(total_df.corr(), annot=True, cmap=cmap)
    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()
    # 결과 양의 상관관계가 있음 0.5 0.5

    df_x = pd.DataFrame({
        'x1': Index_x,
        'x2': pop2019
    })

    results = sm.OLS(Index_y_1, sm.add_constant(df_x)).fit()
    print(results.summary())

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2019, Index_y_1)

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()

    ploty = list()
    for i in range(0, len(Index_x)):
        ploty.append(Index_x[i] * 0.4213 + pop2019[i] * 0.0003 + 277.3284)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(Index_x, pop2019, Index_y_1)
    ax.scatter(Index_x, pop2019, ploty, c='black')

    plt.title('few crimes and the number of CCTVs in each Seoul district office in 2019 with pop_infore')
    plt.show()

    #서울지도로 CCTV과잉 부족 2019년도 기준으로 나타내기
    r = requests.get(
        'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
    c = r.content
    seoul_geo = json.loads(c)

    m=folium.Map(
        location=[37.566345, 126.977893],
        zoom_start=11
    )
    state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'


    total_region = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구',
                    '강북구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구',
                    '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구','도봉구']
    lista = list()
    for i in range(0,len(Index_x)):
        lista.append(ploty[i]-Index_y_1[i])#+이면 과잉 -면 부족
    lista.append(0)
    df = pd.DataFrame({
        '지역구': total_region,
        '과잉혹은부족': lista
    })
    folium.GeoJson(
        seoul_geo,
        name='CCTV'
    ).add_to(m)

    m.choropleth(geo_data=state_geo,
                 data=df,
                 columns=['지역구','과잉혹은부족'],
                 fill_color='YlOrRd',  # 색상 변경도 가능하다
                 key_on='properties.name',
                 legend_name="cctv over or less"
                 )
    m.save('kr_incode.html')






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
