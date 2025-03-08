# pytest-postgres
【目標】  
postgresqlをDBとして利用し、pytest実行時に既存のデータに影響がない仕組みを作成する。

【背景】  
プロジェクトでpytest + python + postgresqlを利用している。  
テスト用にDBを分けていないため、テスト実行語にDB内のデータが削除され、テスト時に作成したテストデータのみとなってしまう。  
テストを動かす度にデータが消えてしまうと、ローカルでの動作確認時に不便。  


## TODO
- [x] docker環境構築
- [x] postgresql 環境セットアップ
- [ ] python, postgresql 間での疎通確認
- [ ] 簡単なCRUD処理追加
- [ ] pytest追加
- [ ] 既存のデータに影響がないテスト環境の検討、作成