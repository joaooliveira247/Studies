 var hour = new Date().getHours();
      var greeting;

      if (hour < 12) {
        greeting = "Good Morning 🌄";
      } else if (hour >= 12 && hour < 18) {
        greeting = "Good AfterNoon ☕";
      } else {
        greeting = "Good Evening 🌛";
      }

      document.getElementById("msg").innerHTML = greeting;