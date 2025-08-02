class CreateNamespaces < ActiveRecord::Migration[8.0]
  def change
    create_table :namespaces do |t|
      t.string :label
      t.string :uri

      t.timestamps
    end
  end
end
