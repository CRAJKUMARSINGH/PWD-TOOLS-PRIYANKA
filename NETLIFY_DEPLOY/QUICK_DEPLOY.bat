@echo off
echo ========================================
echo PWD Tools Suite - Netlify Deployment
echo ========================================
echo.

echo Checking Netlify CLI...
where netlify >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Netlify CLI not found!
    echo.
    echo Please install it first:
    echo   npm install -g netlify-cli
    echo.
    pause
    exit /b 1
)

echo Netlify CLI found!
echo.

echo Logging in to Netlify...
netlify login

echo.
echo Initializing site...
netlify init

echo.
echo Deploying to production...
netlify deploy --prod

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your app is now live on Netlify!
echo Check the URL above to access it.
echo.
pause
