with source_data as (
    select *
    from {{ref('My_model')}}
),
final as (
    select vehicle_type,
        COUNT(*)
    from source_data
    group by vehicle_type
)
SELECT *
FROM final