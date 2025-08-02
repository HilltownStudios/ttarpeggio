class NamespacesController < ApplicationController
  before_action :set_namespace, only: %i[ show edit update destroy ]
  allow_unauthenticated_access only: %i[ index show ]
  def index
    @namespaces = Namespace.all
  end

  def show
  end

  def new
    @namespace = Namespace.new
  end

  def create
    @namespace = Namespace.new(namespace_params)
    if @namespace.save
      redirect_to @namespace
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
  end

  def update
    if @namespace.update(namespace_params)
      redirect_to @namespace
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @namespace.destroy
    redirect_to namespaces_path
  end

  private
    def set_namespace
      @namespace = Namespace.find(params[:id])
    end

    def namespace_params
      params.expect(namespace: [ :label, :uri ])
    end
end
