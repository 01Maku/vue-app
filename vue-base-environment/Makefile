# Use make scripts if you are running this app on UNIX environment
# Refer root: package.json if you are running on WINODWS environment
# Makefile for running Vue app development server

FRONTEND_DIR = frontend

app-start:
	npm run serve
	
# Build the frontend dependencies
app-build-frontend:
	cd $(FRONTEND_DIR) && \
	npm install && \
	@docker-compose build frontend

# Run the Docker container
docker-up:
	@docker-compose up

# Stop the Docker container
docker-down:
	@docker-compose down