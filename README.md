# TwitterOpenAPIs
## 프로젝트 계획 이유
> 트위터는 사진·동영상·음성녹음·웹링크·단문 등 다양한 데이터 유형으로 구성된 트윗이라는 메시지를 280자 이내로 게시해 서로 소통하는 세계적으로 유명한 온라인 소셜네트워크 서비스다. 표1는 트윗에 포함될 수 있는 다양한 데이터 유형을 보여준다. 트위터는 2018년 월간 활동 사용자(MAU)가 3억3600만 명에 달했고, 2020년 4분기에는 수익형 일일 활동 트위터 사용자(mDAU)가 1억9200만 명에 이른다고 보도했다 [1]. 또한 초당 약 6,000개의 트윗이 생성되어 분당 약 350만 개, 하루에 5억 개, 연간 2,000억 개의 트윗이 생성되고 있음을 알 수 있다 [2].
트위터 사용자들은 트윗을 통해 서로 소통하고, 생각과 정보를 공유하고, 속보를 얻고, 조언을 구할 수 있다. 트위터 데이터의 실시간적이고 개방적인 특성 때문에, 트윗은 마케팅, 광고, 예측 분석 등 다양한 비즈니스와 연구 분야에서 널리 사용되어 왔다. 사카키 외 연구진 [3]에서 지진과 같은 이벤트를 감지했습니다. 레이즈 외 연구진 [4]은(는) 비유적 언어를 포함하는 트윗 데이터에서 패턴을 발견하고 이를 두 가지 범주(즉, 유머와 아이러니)로 자동 분류하는 방법을 보여주었다. 알마스 외 연구진 [5]은 다양한 주제와 정서 정보를 사용하여 계층적으로 사용자 태도에 대한 모델을 구성하여 트윗 데이터를 사용하여 정서 분석을 수행하는 새로운 확률적 모델을 제안했다. Aggarwal 외 연구진 [6]는 트윗을 사용하여 비트코인 가격 변화를 예측하는 방법을 제안했고 아브라함 등은 트윗 데이터와 구글 트렌드 데이터를 활용하여 비트코인과 이더리움 가격의 변화를 예측하는 방법을 제시했다 [7]. 썬 외 연구진[8] 및 쑤 외 연구진 [9]이 트윗 데이터를 이용해 주식시장을 예측했다. 호세인 외 연구진[10]은 영화 관련 트윗 데이터를 분석해 영화의 재정적인 성공을 예측했다. 루 외 연구진 [11]은 트윗 데이터에서 새로운 주제 동향을 식별했습니다. 굴 외 연구진 [12]은(는) 금융대책뿐 아니라 트윗 데이터를 활용해 회사의 신뢰도를 결정하는 신용등급 접근법을 제안했다. 렛트 외 연구진 [13]은 트윗에 숨겨진 다양한 기능을 추출하여 각 사용자가 생성한 트윗 데이터가 고유한 속성을 가지며 사용자의 라이프 측면을 반영한다고 주장했다. 따라서 분석 목적을 충족시키기 위해 전체 트윗을 수집할 필요가 있는데, 이는 특정 트윗 사용자 그룹이나 대상 키워드 집합일 수 있다. 그러나 우리가 아는 한, 아무런 제한 없이 전체 트윗을 크롤링하는 방법은 없다. ![image](https://user-images.githubusercontent.com/49609287/123900337-d9afb600-d9a3-11eb-99ec-4450ba7475ac.png)


## Reference
# [1]	Twitter statistics, available online, https://investor.twitterinc.com/ home/default.aspx, accessed on 14 April 2021. 
[2]	Twitter statistics, available online, https://www.internetlivestats. com/twitter-statistics/, accessed on 14 April 2021. 
[3]	T. Sakaki, M. Okazaki, Y. Matsuo, Tweet analysis for real-time event detection and earthquake reporting system development, IEEE Transactions on Knowledge and Data Engineering 25 (4) (2012) 919–931. 
[4]	A. Reyes, P. Rosso, D. Buscaldi, From humor recognition to irony detection: The figurative language of social media, Data & Knowledge Engineering 74 (2012) 1–12. 485 
[5]	A. Almars, X. Li, X. Zhao, Modelling user attitudes using hierarchical sentiment-topic model, Data & Knowledge Engineering 119 (2019) 139– 149. 
[6]	J. Abraham, D. Higdon, J. Nelson, J. Ibarra, Cryptocurrency price prediction using tweet volumes and sentiment analysis, SMU Data Science 490 Review 1 (3) (2018) 1. 
[7]	[7] A. Aggarwal, I. Gupta, N. Garg, A. Goel, Deep learning approach to determine the impact of socio economic factors on bitcoin price prediction, 25 in: 2019 Twelfth International Conference on Contemporary Computing (IC3), IEEE, 2019, pp. 1–5. 495 
[8]	A. Sun, M. Lachanski, F. J. Fabozzi, Trade the tweet: Social media text mining and sparse matrix factorization for stock market prediction, International Review of Financial Analysis 48 (2016) 272–281. 
[9]	Y. Xu, S. B. Cohen, Stock movement prediction from tweets and historical prices, in: Proceedings of the 56th Annual Meeting of the Association for 500 Computational Linguistics (Volume 1: Long Papers), 2018, pp. 1970–1979. 
[10]	N. Hossein, D. W. Miller, Predicting motion picture box office performance using temporal tweet patterns, International Journal of Intelligent Computing and Cybernetics. 
[11]	R. Lu, Q. Yang, Trend analysis of news topics on twitter (2012). 
[12]	S. G¨ul, O. Kabak, I. Topcu, A multiple criteria credit rating approach ¨ 505 utilizing social media data, Data & Knowledge Engineering 116 (2018) 80– 99. 
[13]	S. R, J. Pujari, V. S. Bhat, A. Dixit, Timeline Analysis of Twitter User, Procedia Computer Science 132 (2018) 157–166. 510 doi:https://doi.org/10.1016/j.procs.2018.05.179. URL https://www.sciencedirect.com/science/article/pii/ S187705091830913X
![image](https://user-images.githubusercontent.com/49609287/123900420-01068300-d9a4-11eb-992b-11047cf0810a.png)
