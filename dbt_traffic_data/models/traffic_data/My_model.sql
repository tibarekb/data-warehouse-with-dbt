with source_data_cast as (
    select *
    from {{ source('test', 'traffic_data') }}
),
final as (
    select id,
        track_id,
        type as vehicle_type,
        traveled_d,
        avg_speed,
        lat,
        lon,
        speed,
        lon_acc,
        lat_acc,
        time as vtime
    from source_data_cast
)
SELECT *
FROM final