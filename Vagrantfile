# -*- mode: ruby -*-
# vi: set ft=ruby

# created by {{cookiecutter.author}}

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_version ">= 1.6.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
	config.vm.define "postgres" do |a|
		a.vm.provider :docker do |d|
			d.image = "postgres"
			d.env = {
					POSTGRES_USER: "dev",
					POSTGRES_PASSWORD: "dev",
					POSTGRES_DB: "ares"
			}
			d.name = "ares-postgres"
			d.ports = ["5432:5432"]
		end
	end

	config.vm.define "redis" do |a|
		a.vm.provider :docker do |d|
			d.image = "redis"
			d.name = "ares-redis"
			d.create_args = ["-d"]
			d.ports = ["6379:6379"]
		end
	end

	config.vm.define "dev-box" do |a|
		a.vm.provider :docker do |d|
			d.build_dir = "."
			d.name = "ares"
			d.env = {
					PG_HOSTNAME: "postgres",
					PG_USERNAME: "dev",
					PG_PASSWORD: "dev"
			}
			d.link "ares-postgres:postgres"
			d.link "ares-redis:redis"
			d.has_ssh = false
			d.ports = ["5000:5000"]
		end
		a.vm.synced_folder ".", "/project"
	end
end