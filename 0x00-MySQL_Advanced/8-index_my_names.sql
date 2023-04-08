-- create index on table idx_name_first on names taking the first letter
CREATE INDEX idx_name_first ON names (name(1));
