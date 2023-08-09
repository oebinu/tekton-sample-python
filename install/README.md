# https://tekton.dev/docs/installation/triggers/

## 문서 내용 그대로 복사
kubectl apply --filename \
https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
kubectl apply --filename \
https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml



## 사용한 코드
wget https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
mv release.yaml trigger_v0.24.1.yaml
wget https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml
mv interceptors.yaml interceptors_v0.24.1.yaml