## 構成図
![english_reading_support_app_architecture](https://github.com/user-attachments/assets/142bdbe0-6e44-4a2b-be8f-dce6f7d05b58)

アプリ全体の構成
メインアプリ（Django on ECS Fargate）

DjangoアプリはECS Fargateでホストされ、ユーザーのフロントエンドインターフェースを提供します。
ユーザーが翻訳・要約機能をリクエストすると、DjangoアプリがLambda関数を通してAPIリクエストを行い、AWS Bedrockでの処理を行います。
翻訳・要約API（Lambda + Bedrock）

各種機能（翻訳、要約）はLambda関数として設置され、Djangoからリクエストを受け取ります。
AWS Bedrockを利用して、翻訳や要約処理を行います。Lambda関数でBedrockのAPIを呼び出し、生成された翻訳や要約結果をDjangoに返します。
要約結果に元の文書URLを添付し、出典情報も付与します。
単語保存機能（DynamoDB + Lambda）

DynamoDBにユーザーごとにわからなかった単語を保存し、Djangoアプリから保存や取得が可能にします。Lambdaを通じてCRUD操作が可能です。
アーキテクチャ
ECS Fargate：メインのDjangoアプリケーションをホスト
Lambda：API Gatewayを介してDjangoからのリクエストを受け、翻訳・要約処理や単語保存操作を担当
Bedrock：Lambda関数内で利用し、生成AIによる翻訳・要約を実行
DynamoDB：単語データの保存用データベース
TerraformでこれらのAWSリソースを定義することで、迅速にインフラを構築できます。設計やコードについてさらに具体的な例が必要であれば、お知らせください。
