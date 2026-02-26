@echo off
echo ========================================
echo Update Existing Netlify Site
echo https://pwd-tools-priyanka.netlify.app
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
echo Linking to existing site: pwd-tools-priyanka
netlify link --name pwd-tools-priyanka

echo.
echo Deploying updates to production...
netlify deploy --prod --dir=.

echo.
echo ========================================
echo Update Complete!
echo ========================================
echo.
echo Your site has been updated at:
echo https://pwd-tools-priyanka.netlify.app
echo.
pause
