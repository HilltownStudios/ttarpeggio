class Namespace < ApplicationRecord
  validates :label, presence: true
  validates :uri, presence: true
end
