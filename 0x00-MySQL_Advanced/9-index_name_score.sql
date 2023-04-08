-- a script that creates an index idx_name_first_score
--on the table first letter of names and the score.
CREATE INDEX idx_name_first_score ON names(name(1), score);
