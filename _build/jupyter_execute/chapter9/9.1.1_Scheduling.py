#!/usr/bin/env python
# coding: utf-8

# ### 윈도우즈 스케줄러
# 
# 오전 9시에 파이썬 프로그램이 자동으로 실행이 되게 윈도우즈 스케줄링 해 보겠습니다. 우선 실행창에 아래와 같이 타이핑하여 스케줄러를 오픈합니다. 

# ![GET_IMAGE](images/cmd_window.PNG)

# ![GET_IMAGE](images/scheduler.PNG)

# 오른쪽 '작업만들기' 버튼을 클릭하여 새로운 작업을 생성합니다. 간단하 이름과 설명을 넣어주고 마지막에 '가장 높은 수준의 권한으로 실행' 을 체크합니다. 이제 '트리거'와 '동작'을 설정하면 됩니다. 

# ![GET_IMAGE](images/new_task.PNG)

# '트리거' 탭에서 [새로만들기]로 들어가 작업 설정을 해 줍니다. 매주에서 월요일부터 금요일까지 선택을 하고, 시작시간을 9시00분으로 설정해줍니다.

# ![GET_IMAGE](images/Trigger.PNG)

# 그 다음 동작탭으로 가서 파이썬 실행파일 위치를 지정해줍니다. '프로그램/스크립트' 칸에는 우리가 사용할 python.exe 의 위치, '인수 추가' 칸에는 작성한 실행코드 파일, 마지막으로 시작 위치는 '작성한 파이썬 코드'의 위치를 넣어줍니다. 이제 스케줄링이 끝났습니다. 매주 월요일부터 금요일까지 9시에 파이썬 코드가 자동으로 실행됩니다. 

# ![GET_IMAGE](images/Action.PNG)

# In[ ]:




