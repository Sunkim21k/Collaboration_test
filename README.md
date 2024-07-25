# Collaboration_test
PC환경과 노트북환경 git과 github협업 적응용

**PC환경**
- 메인 github계정으로 git terminal 사용
- develop 브랜치 충돌 점검과 main PR 승인

**노트북환경**
- 서브 github계정으로 파이참 git GUI 사용
- develop 브랜치 push와 main PR

1. 노트북 서브 github계정으로 알고리즘 풀이후 develop branch push 및 main PR
2. 메인 github계정으로 알고리즘 정답시 승인후 main merge / 틀릴시 재검토요청후 1번수행
3. 메인 github계정으로 알고리즘 풀이후 develop branch push
4. 1번과 3번을 섞어서 반복 develop merge 충돌 점검
5. develop이 쌓이면 main merge
