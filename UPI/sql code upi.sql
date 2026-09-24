WITH Remitter_Totals AS (
	SELECT 
		Bank_Name,
        SUM(Remitter_Vol_Mn) AS Total_Sent_Mn
	FROM bank_data
    GROUP BY Bank_Name
),
Beneficiary_Totals AS (
	SELECT 
		Bank_Name,
        SUM(Beneficiary_Vol_Mn) AS Total_Received_Mn
	FROM bank_data
    GROUP BY Bank_Name
)
SELECT
	r.Bank_Name,
    ROUND(r.Total_Sent_Mn,2) AS Total_Sent_Mn,
    ROUND(b.Total_Received_Mn,2) AS Total_Received_Mn,
    ROUND(b.Total_Received_Mn - r.Total_Sent_Mn,2 ) AS Net_Difference
FROM Remitter_Totals r
JOIN Beneficiary_Totals b
	ON r.Bank_Name = b.Bank_Name
ORDER BY Total_Sent_Mn DESC
LIMIT 10; 