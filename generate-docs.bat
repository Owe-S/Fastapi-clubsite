@echo off
REM — CONFIGURATION ——————————————————————————————————
SET PORT=8000
SET OPENAPI_URL=http://localhost:%PORT%/openapi.json
SET OUT_DIR=docs
SET UI_SRC=node_modules\swagger-ui-dist
SET UI_DST=docs\swagger-ui
REM — END CONFIGURATION ——————————————————————————————

echo.
echo === Fetching OpenAPI spec from %OPENAPI_URL% ===
curl --fail %OPENAPI_URL% -o %OUT_DIR%\swagger.json
IF ERRORLEVEL 1 (
  echo.
  echo [ERROR] Could not fetch spec. Is FastAPI running on port %PORT%?
  echo Exiting.
  exit /b 1
)

echo.
echo === Copying Swagger UI files ===
IF NOT EXIST %UI_DST% (
  mkdir %UI_DST%
)
xcopy %UI_SRC%\* %UI_DST%\ /E /I /Y >nul

echo.
echo ✅ Documentation generated in .\%OUT_DIR%
exit /b 0
