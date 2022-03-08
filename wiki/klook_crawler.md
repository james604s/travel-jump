# klook 爬蟲
爬蟲主要爬露營相關商品及其內文內容。
排程: Daily 00:00:00, cron: 0 0 * * *
> 注意事項 - Headers 相關內容
> * user-agent 需使用且建議更換。
> * cookie 可能會變動, 每次爬蟲須更新。 (尚未完成)
> * accept-language 設為 zh-TW, 否則會吐假資料。
> * currency 設為 TWD, 自動轉換匯率。

MongoDB  
> Collection  
> _ctime 過濾資料, activitiy_id可做關聯
> * activities_list // 露營行程列表
> * activities_rating_info // 露營行程評價

商品評價內容
> Raw Data Filter後的csv  
> 範例: 2022-03-08_klook_activities_rating_info.csv