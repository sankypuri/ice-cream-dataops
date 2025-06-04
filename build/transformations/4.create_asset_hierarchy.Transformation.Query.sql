select
  `external_id` as externalId,
  `name` as name,
  `description` as description,
  if(
      `parent_external_id` == ''
      OR `parent_external_id` == null,
      null,
      node_reference('icapi_dm_space', `parent_external_id`)
  ) as parent
  from
  `ice-cream-factory-db`.`assets`