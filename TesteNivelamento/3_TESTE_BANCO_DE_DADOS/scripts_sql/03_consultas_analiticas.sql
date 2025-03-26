SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(d.saldo_final::numeric) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS%ASSIST%NCIA%SA%DE%MEDICO%HOSPITALAR%'
  AND date_part('year', d.data) = (SELECT MAX(date_part('year', data)) FROM demonstracoes_contabeis)
  AND date_part('quarter', d.data) = (
      SELECT MAX(date_part('quarter', data))
      FROM demonstracoes_contabeis
      WHERE date_part('year', data) = (SELECT MAX(date_part('year', data)) FROM demonstracoes_contabeis)
  )
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(d.saldo_final::numeric) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS%ASSIST%NCIA%SA%DE%MEDICO%HOSPITALAR%'
  AND date_part('year', d.data) = (SELECT MAX(date_part('year', data)) FROM demonstracoes_contabeis)
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;
